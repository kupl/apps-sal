import numpy as np

n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
h = np.array(h)

hi = 10**10
low = -1


def calc(x):
    y = h - x * b
    y[y < 0] = 0
    f = np.ceil(y / (a - b)).sum()
    return f


while hi - low > 1:
    ave = (hi + low) // 2
    if calc(ave) <= ave:
        hi = ave
    else:
        low = ave

print(hi)
