import numpy as np
(a, b, x) = map(int, input().split())
if x >= a ** 2 * b / 2:
    ans = np.arctan(2 * (b - x / a ** 2) / a)
else:
    ans = np.arctan(a * b / 2 / x * b)
print(ans * 180 / np.pi)
