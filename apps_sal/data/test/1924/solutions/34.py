from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key
import heapq


def rsa(sep=''):
    if sep == '':
        return input().split()
    else:
        return input().split(sep)


def rip(sep=''):
    if sep == '':
        return list(map(int, input().split()))
    else:
        return list(map(int, input().split(sep)))


def ria(sep=''):
    return list(rip(sep))


def ri():
    return int(input())


def rd():
    return float(input())


def rs():
    return input()


def inv(v, mod):
    return pow(v, mod - 2, mod)


def main():
    (r1, c1, r2, c2) = rip()
    MM = int(2000000.0 + 10)
    fact = [0] * MM
    finv = [0] * MM
    fact[0] = 1
    finv[0] = 1
    mod = int(1000000000.0) + 7
    for i in range(1, MM):
        fact[i] = fact[i - 1] * i % mod
    '\n    finv[MM-1] = inv(fact[MM-1], mod)\n    for i in reversed(range(1,MM-1)):\n        finv[i] = finv[i + 1] * (i + 1) % mod\n    def sum_naive(r, c):\n        #[0, r) * [0, c)\n        ret = 0\n        for i in range(r):\n            ret += fact[i + 1 + c - 1] * finv[i + 1] * finv[c - 1] % mod\n        return ret\n    def sum(r, c):\n        #[0, r) * [0, c)\n        ret = fact[r + c] * finv[r] * finv[c] % mod\n        ret += -1 + mod\n        ret %= mod\n        return ret\n    '

    def sum(r, c):
        ret = fact[r + c] * inv(fact[r], mod) * inv(fact[c], mod) % mod
        ret += -1 + mod
        ret %= mod
        return ret
    ans = 0
    ans += sum(r2 + 1, c2 + 1)
    ans -= sum(r2 + 1, c1)
    ans -= sum(r1, c2 + 1)
    ans += sum(r1, c1)
    ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
