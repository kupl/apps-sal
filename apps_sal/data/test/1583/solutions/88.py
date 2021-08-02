import numpy as np
a, b, x = map(int, input().split())
if x <= a * a * b / 2:
    y = 2 * x / (a * b)
    print(360 / ((2 * np.pi) / np.arctan(b / y)))
else:
    y = 2 * x / (a**2) - b
    print(360 / ((2 * np.pi) / np.arctan((b - y) / a)))
