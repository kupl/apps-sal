import sys
import numpy as np


N, M = list(map(int, sys.stdin.readline().rstrip().split()))
A = np.array(sys.stdin.readline().rstrip().split(), np.int64)

A.sort()


def shake_cnt(x):
    X = np.searchsorted(A, x - A)
    return N * N - X.sum()


left = 0
right = 10 ** 6
while 1 < right - left:
    x = (left + right) // 2
    if shake_cnt(x) >= M:
        left = x
    else:
        right = x

X = np.searchsorted(A, right - A)
shake = N * N - X.sum()

Acum = np.zeros(N + 1, np.int64)
Acum[1:] = np.cumsum(A)

happy = (Acum[-1] - Acum[X]).sum() + (A * (N - X)).sum()

happy += (M - shake) * left

print(happy)
