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


def JAA(a, s, t):
    return s.join((t.join(map(str, b)) for b in a))


class UnionFind:

    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a


def main():
    n = I()
    xy = [LI() for _ in range(n)]
    xd = {}
    yd = {}
    xi = 0
    yi = 0
    for (x, y) in xy:
        if x not in xd:
            xd[x] = xi
            xi += 1
        if y not in yd:
            yd[y] = yi
            yi += 1
    uf = UnionFind(xi + yi + n)
    ii = xi + yi
    for i in range(n):
        (x, y) = xy[i]
        uf.union(xd[x], ii + i)
        uf.union(xi + yd[y], ii + i)
    dx = collections.defaultdict(set)
    dy = collections.defaultdict(set)
    for i in range(n):
        (x, y) = xy[i]
        ui = uf.find(ii + i)
        dx[ui].add(x)
        dy[ui].add(y)
    r = -n
    for (k, xv) in dx.items():
        yv = dy[k]
        r += len(xv) * len(yv)
    return r


print(main())
