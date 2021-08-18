import numpy as np
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A = np.array(A)
F = np.array(F)

A = np.sort(A)[::-1]
F = np.sort(F)
B = np.sum(A)
M = max([a * f for a, f in zip(A, F)])


def is_possible(x):
    return B - np.minimum(A, x // F).sum() <= K


left = -1
right = M
while left + 1 < right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid
    else:
        left = mid

print(right)
