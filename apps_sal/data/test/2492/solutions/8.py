import numpy as np
import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


def resolve():
    (N, K) = lr()
    A = np.sort(np.array(lr(), np.int64))
    z = A[A == 0]
    p = A[A > 0]
    n = A[A < 0]

    def count_func(x):
        cnt = 0
        if x >= 0:
            cnt += len(z) * N
        cnt += np.searchsorted(A, x // p, side='right').sum()
        cnt += (N - np.searchsorted(A, -(-x // n), side='left')).sum()
        cnt -= np.count_nonzero(A * A <= x)
        assert cnt % 2 == 0
        return cnt // 2
    l = -10 ** 18
    r = 10 ** 18
    while l + 1 < r:
        x = (l + r) // 2
        if count_func(x) >= K:
            r = x
        else:
            l = x
    print(r)


resolve()
