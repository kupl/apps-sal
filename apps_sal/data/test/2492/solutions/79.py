import numpy as np
from numba import njit


@njit
def main(I):
    N, K = I[0], I[1]
    A = I[2:]
    A.sort()
    lb = -10**18 - 1
    rb = 10 ** 18 + 1
    while rb - lb > 1:
        target = (rb + lb) // 2
        if 1:
            cnt = 0
            for i, a in enumerate(A):
                if a == 0:
                    d = i if target >= 0 else 0
                elif a < 0:
                    il = np.searchsorted(A, 0 - (-target) // a, side='left')
                    d = max(i - il, 0)
                else:
                    ir = np.searchsorted(A, target // a, side='right')
                    d = min(ir, i)
                cnt += d
        if cnt >= K:
            rb = target
        else:
            lb = target
    return rb


I = np.array([int(_) for _ in open(0).read().split()], dtype=int)
print(main(I))
