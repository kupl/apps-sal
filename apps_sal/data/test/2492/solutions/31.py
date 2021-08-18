import numpy as np


def resolve():
    n, k = map(int, input().split())
    a = np.array(input().split(), dtype=np.int64)
    a.sort()

    zero = np.count_nonzero(a == 0)
    positive = a[a > 0]
    negative = a[a < 0]

    def count(x):
        ans = 0
        if x >= 0:
            ans += n * zero
        ans += np.searchsorted(a, x // positive, side="right").sum()
        ans += n * len(negative) - np.searchsorted(a, -(-x // negative), side="left").sum()
        ans -= np.count_nonzero(a * a <= x)
        return ans // 2

    ok = 10 ** 18
    ng = -ok - 1
    while ok - ng > 1:
        cen = (ok + ng) // 2
        if count(cen) >= k:
            ok = cen
        else:
            ng = cen
    print(ok)


def __starting_point():
    resolve()


__starting_point()
