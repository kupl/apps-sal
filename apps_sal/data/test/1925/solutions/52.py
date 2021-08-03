import numpy as np
a, b, n = map(int, input().split())

if b - 1 <= n:
    value = np.floor(a * (b - 1) / b) - a * np.floor((b - 1) / b)
else:
    value = np.floor(a * n / b) - a * np.floor(n / b)
print(int(value))
