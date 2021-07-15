#!/usr/bin/env python3
from functools import reduce
from operator import mul

mod = 10**9 + 7


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(lambda a, b: a * b % mod, list(range(n, n - r, -1)))
    under = reduce(lambda a, b: a * b % mod, list(range(1, r + 1)))
    return over * pow(under,mod-2,mod)


n, a, b = list(map(int, input().split()))
print(((pow(2, n, mod) - 1 - cmb(n, a) - cmb(n, b)) % mod))

