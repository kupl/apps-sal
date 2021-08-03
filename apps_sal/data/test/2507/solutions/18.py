import numpy as np
from numba import njit

n, k = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
F = np.array(list(map(int, input().split())))

A = np.sort(A)
F = np.sort(F)[::-1]


@njit
def is_ok(x):
    tmp = 0
    for a, f in zip(A, F):
        y = a * f
        if y > x:
            tmp += a - x // f
    return tmp <= k


ok = 10 ** 16
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
