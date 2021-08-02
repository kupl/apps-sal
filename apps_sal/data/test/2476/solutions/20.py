from bisect import bisect_left
from math import floor
from itertools import accumulate
from collections import Counter
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))

    c = Counter(a)
    c = list(c.values())

    d = Counter(c)
    d_li = [0] * (n + 1)
    for k, v in list(d.items()):
        d_li[k] = v

    dk_acm = list(accumulate(d_li))

    kdk_acm = [0]
    for k, e in enumerate(d_li[1:], 1):
        kdk_acm.append(kdk_acm[-1] + k * e)

    def f(x):
        kdk_sm = kdk_acm[x]
        dk_sm = dk_acm[n] - dk_acm[x]

        return floor((kdk_sm + x * dk_sm) / x)

    fs = [float("inf")] + [f(x) for x in range(1, n + 1)]
    fs = fs[::-1]

    for k in range(1, n + 1):
        print((n - bisect_left(fs, k)))


def __starting_point():
    main()


__starting_point()
