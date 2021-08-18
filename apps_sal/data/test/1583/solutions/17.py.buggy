import numpy as np

a, b, x = map(int, input().split())

if x == a**2 * b:
    print(0)
    return

if x < 1 / 2 * b * a**2:
    a1 = 2 * x / (a * b)
    rad = np.arctan(a1 / b)
else:
    y = 2 * (b - x / a**2)
    rad = np.arctan(a / y)

print(90 - rad * 180 / np.pi)
