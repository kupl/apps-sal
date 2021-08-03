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
import time
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


class Prime():
    def __init__(self, n):
        self.M = m = int(math.sqrt(n)) + 10
        self.A = a = [True] * m
        a[0] = a[1] = False
        self.T = t = [2]
        for j in range(4, m, 2):
            a[j] = False
        for i in range(3, m, 2):
            if not a[i]:
                continue
            t.append(i)
            for j in range(i * i, m, i):
                a[j] = False
        self.ds_memo = {}
        self.ds_memo[1] = set([1])

    def is_prime(self, n):
        return self.A[n]

    def division(self, n):
        d = collections.defaultdict(int)
        for c in self.T:
            while n % c == 0:
                d[c] += 1
                n //= c
            if n < 2:
                break
        if n > 1:
            d[n] += 1
        return d.items()

    # memo
    def divisions(self, n):
        if n in self.ds_memo:
            return self.ds_memo[n]

        for c in self.T:
            if n % c == 0:
                rs = set([c])
                for cc in self.divisions(n // c):
                    rs.add(cc)
                    rs.add(cc * c)
                self.ds_memo[n] = rs
                return rs

        rs = set([n])
        self.ds_memo[n] = rs
        return rs


def main():
    n = I()

    pr = Prime(10**12)
    d = list(pr.division(n))
    r = 0
    l = len(d)
    for i in range(1, 2**l):
        t = [d[j] for j in range(l) if 2**j & i]
        m = min(map(lambda x: x[1], t))
        ok = True
        for k, v in t:
            if v % m > 0:
                ok = False
                break
        if not ok:
            continue
        for j in range(1, m + 1):
            if m % j > 0:
                continue
            mk = m // j
            u = 1
            for k, v in t:
                u *= k**((v // m) * mk)
            nn = n
            while nn % u == 0:
                nn //= u
            if nn % u == 1:
                r += 1
            # print("u",u,j,nn,r)

    d = pr.division(n - 1)
    # print("d",d)
    k = 1
    for _, v in d:
        k *= v + 1
    r += k - 1

    return r


print(main())
