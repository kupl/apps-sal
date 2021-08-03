import numpy as np
base = 10**9 + 7


def pw(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((pw(x, n // 2)**2 % base) * pw(x, n % 2) % base)


n = int(input())
print((pw(10, n) - 2 * pw(9, n) + pw(8, n)) % base)
