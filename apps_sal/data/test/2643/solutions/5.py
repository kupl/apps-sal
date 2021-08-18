import numpy as np
import sys
sysread = sys.stdin.readline
sys.setrecursionlimit(10**7)


def run():
    k, q = map(int, sysread().split())
    d = list(map(int, sysread().split()))
    d = np.array(d, dtype=np.uint64)

    def check(n, x, m):
        _d = d % m
        d0 = d % m == 0
        n_d = (n - 1) // k
        n_rest = (n - 1) % k
        x %= m
        _d_rest, d0_rest = 0, 0
        if n_rest != 0:
            _d_rest = _d[:n_rest].sum()
            d0_rest = d0[:n_rest].sum()

        a_last = x + n_d * _d.sum() + _d_rest
        n_step = a_last // m
        n_same = n_d * d0.sum() + d0_rest

        return n - 1 - n_same - n_step

    for _ in range(q):
        n, x, m = map(int, sysread().split())
        print(int(check(n, x, m)))


def __starting_point():
    run()


__starting_point()
