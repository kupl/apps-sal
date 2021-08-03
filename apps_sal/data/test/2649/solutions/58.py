import numpy as np


def solve(n, x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    z = x + y
    w = x - y
    return max(np.max(z) - np.min(z), np.max(w) - np.min(w))


n = int(input())
x, y = list(zip(*[list(map(int, input().split())) for i in range(n)]))
print((solve(n, x, y)))
