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

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [tuple(map(int, l.split())) for l in sys.stdin]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


class Seg():
    def __init__(self, na, default, func):
        if isinstance(na, list):
            n = len(na)
        else:
            n = na
        i = 1
        while 2**i <= n:
            i += 1
        self.D = default
        self.H = i
        self.N = 2**i
        if isinstance(na, list):
            self.A = [default] * (self.N) + na + [default] * (self.N - n)
            for i in range(self.N - 1, 0, -1):
                self.A[i] = func(self.A[i * 2], self.A[i * 2 + 1])
        else:
            self.A = [default] * (self.N * 2)
        self.F = func

    def find(self, i):
        return self.A[i + self.N]

    def update(self, i, x):
        i += self.N
        self.A[i] = x
        while i > 1:
            i = i // 2
            self.A[i] = self.merge(self.A[i * 2], self.A[i * 2 + 1])

    def merge(self, a, b):
        return self.F(a, b)

    def total(self):
        return self.A[1]

    def query(self, a, b):
        A = self.A
        l = a + self.N
        r = b + self.N
        res = self.D
        while l < r:
            if l % 2 == 1:
                res = self.merge(res, A[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.merge(res, A[r])
            l >>= 1
            r >>= 1

        return res


def main():
    n, m = LI()
    a = list(map(lambda x: (x, 0), LI()))
    q = [LI() for _ in range(m)]

    def f(a, b):
        if a[1] % 2 == 0:
            return (a[0] | b[0], 1)
        return (a[0] ^ b[0], 0)

    seg = Seg(a, (0, 0), f)
    r = []
    for i, t in q:
        seg.update(i - 1, (t, 0))
        r.append(seg.total()[0])

    return '\n'.join(map(str, r))


print(main())
