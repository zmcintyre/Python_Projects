import pyautogui
import time

print("Contorl+C to Exit")

i = 1

while i > 0:
    pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
    time.sleep(10)
    pyautogui.moveTo(None, 500)  # moves mouse to X of 100, Y of 500.
    time.sleep(10)
    pyautogui.moveTo(600, None)  # moves mouse to X of 600, Y of 500.
    time.sleep(10)
    pass
