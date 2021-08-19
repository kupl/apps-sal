from sys import stdin
import numpy as np


def main():
    readline = stdin.readline
    (n, k) = map(int, readline().split())
    a = np.array(readline().strip().split(), dtype='int64')
    a.sort()
    neg = a[a < 0]
    neg_p = neg ** 2
    zero = a[a == 0]
    pos = a[a > 0]
    pos_p = pos ** 2
    l = -10 ** 18 - 1
    r = 10 ** 18
    while l < r - 1:
        x = (l + r) // 2
        cnt = 0
        if len(neg) > 0:
            cnt += (len(a) - np.searchsorted(a, (x + neg + 1) // neg)).sum()
            cnt -= len(neg_p[neg_p <= x])
        if len(zero) > 0:
            if x >= 0:
                cnt += (len(a) - 1) * len(zero)
        if len(pos) > 0:
            cnt += np.searchsorted(a, x // pos, side='right').sum()
            cnt -= len(pos_p[pos_p <= x])
        cnt //= 2
        if cnt >= k:
            r = x
        else:
            l = x
    print(r)


def __starting_point():
    main()


__starting_point()
