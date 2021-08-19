import heapq as hq
import itertools
import math
import collections


def ma():
    return map(int, input().split())


def lma():
    return list(map(int, input().split()))


def tma():
    return tuple(map(int, input().split()))


def ni():
    return int(input())


def yn(fl):
    return print('Yes') if fl else print('No')


ceil = math.ceil


class unionfind:

    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.size = [1] * n
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            if self.rank[x] < self.rank[y]:
                (x, y) = (y, x)
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def get_size(self, x):
        x = self.root(x)
        return self.size[x]

    def parent_set(self):
        for x in range(self.n):
            self.root(x)
        s = set()
        for par in self.par:
            s.add(par)
        return s


(n, m) = ma()
uf = unionfind(n)
for i in range(m):
    (x, y, z) = ma()
    uf.unite(x - 1, y - 1)
s = uf.parent_set()
print(len(s))
