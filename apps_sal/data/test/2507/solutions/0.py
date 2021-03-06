import sys
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(N, K) = lr()
A = np.array(lr())
F = np.array(lr())
A.sort()
F = np.sort(F)[::-1]


def check(x):
    count = np.maximum(0, A - x // F).sum()
    return count <= K


left = 10 ** 12
right = -1
while left > right + 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
