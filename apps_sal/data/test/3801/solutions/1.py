import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import copy
import functools
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def pf(s):
    return print(s, flush=True)


def pe(s):
    return print(str(s), file=sys.stderr)


def JA(a, sep):
    return sep.join(map(str, a))


def inv(x):
    return pow(x, mod - 2, mod)


def main():
    (n, m) = LI()
    a = LI()
    w = LI()

    def plus(a, b):
        c = a[0] * b[1] % mod
        d = b[0] * a[1] % mod
        e = a[1] * b[1] % mod
        return [(c + d) % mod, e]

    def sub(a, b):
        c = a[0] * b[1] % mod
        d = -b[0] * a[1] % mod
        e = a[1] * b[1] % mod
        return [(c + d) % mod, e]

    def mul(a, b):
        c = a[0] * b[0] % mod
        d = a[1] * b[1] % mod
        return [c, d]
    fm = {}

    def f(c, a, m, p, q):
        if m == 0 or c == 0:
            return [c, 1]
        key = (c, a, m, p, q)
        if key in fm:
            return fm[key]
        s = c + p + q
        x = f(c + a, a, m - 1, p, q)
        r = mul(x, [c, s])
        if p > 0:
            y = f(c, a, m - 1, p + 1, q)
            r = plus(r, mul(y, [p, s]))
        if q > 0:
            z = f(c, a, m - 1, p, q - 1)
            r = plus(r, mul(z, [q, s]))
        fm[key] = r
        return r
    ps = 0
    qs = 0
    for i in range(n):
        if a[i] == 1:
            ps += w[i]
        else:
            qs += w[i]
    r = []
    for i in range(n):
        if a[i] == 1:
            v = f(w[i], 1, m, ps - w[i], qs)
        else:
            v = f(w[i], -1, m, ps, qs - w[i])
        r.append(v[0] * inv(v[1]) % mod)
    return JA(r, '\n')


print(main())
