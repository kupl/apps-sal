from datetime import datetime


def is_leap(y):
    return bool((not (y % 4) and (y % 100)) or not (y % 400))


y = int(input())
z = 0
x = y
while True:
    x += 1
    if is_leap(x):
        z += 2
    else:
        z += 1
    if (z % 7) == 0 and is_leap(x) == is_leap(y):
        break
print(x)
