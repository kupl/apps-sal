import numpy as np
from numba import njit
(N, K) = [int(_) for _ in input().split()]
A = np.array(sorted([int(_) for _ in input().split()]))


@njit
def solve(N, K, A):
    lb = -10 ** 18 - 1
    rb = 10 ** 18 + 1

    def check(x):
        cnt = 0
        for (i, a) in enumerate(A):
            l = 0
            r = i
            if a > 0:
                l = -1
                r = np.searchsorted(A, x // a, side='right')
            elif a < 0:
                l = np.searchsorted(A, 0 - x // -a, side='left')
                r = N + 1
            elif x < 0:
                r = 0
            l = min(max(l, 0), i)
            r = max(min(r, i), 0)
            cnt += r - l
        return cnt >= K
    while rb - lb > 1:
        mid = (rb + lb) // 2
        if check(mid):
            rb = mid
        else:
            lb = mid
    print(rb)


solve(N, K, A)
