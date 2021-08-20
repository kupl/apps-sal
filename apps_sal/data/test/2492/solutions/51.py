import numpy as np
(N, K) = list(map(int, input().split()))
A = np.array(tuple(map(int, input().split())), dtype=np.int64)
A = np.sort(A)
pos = A[A > 0]
neg = A[A < 0]
zero = len(A[A == 0])


def cnt(x):
    """return #{a <= x | a in A}"""
    ret = 0
    if x >= 0:
        ret += zero * N
    ret += np.searchsorted(A, x // pos, side='right').sum()
    ret += (N - np.searchsorted(A, (-x - 1) // -neg, side='right')).sum()
    ret -= (A * A <= x).sum()
    return ret // 2


overEq = 10 ** 18 + 100
less = -10 ** 18 - 100
while less + 1 < overEq:
    mid = (overEq + less) // 2
    if cnt(mid) >= K:
        overEq = mid
    else:
        less = mid
print(overEq)
