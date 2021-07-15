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
import random
import time
inf = 10**9


class UnionFind():

    def __init__(self, n: int):
        """
        自身が親であれば、その集合に属する頂点数に-1を掛けたもの
        そうでなければ親のid
        """
        self.r = [-1]*n

    def root(self, x: int):
        if self.r[x] < 0:
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]

    def unite(self, x: int, y: int):
        x, y = self.root(x), self.root(y)
        if x == y:
            return
        if self.r[x] > self.r[y]:
            x, y = y, x
        self.r[x] += self.r[y]
        self.r[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)


def main():
    n, m = list(map(int, input().split()))
    uf = UnionFind(n)
    for i in range(m):
        a, b = list(map(int, input().split()))
        uf.unite(a-1, b-1)
    print((-min(uf.r)))


def __starting_point():
    main()

__starting_point()
