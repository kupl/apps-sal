import collections
import math
import sys


def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7

#import numpy as np

sys.setrecursionlimit(1000000)


class UnionFind():
    par = []

    def __init__(self, n):
        for i in range(n):
            self.par.append(i)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.par[y] = x

    def comp(self):  # rootまでの距離圧縮
        for i in range(len(self.par)):
            self.root(i)


n, m, k = L()
uf = UnionFind(n)
f = [0] * n
for i in range(m):
    a, b = L()
    uf.unite(a - 1, b - 1)
    f[a - 1] += 1
    f[b - 1] += 1
uf.comp()

for i in range(k):
    a, b = L()
    if uf.par[a - 1] == uf.par[b - 1]:
        f[a - 1] += 1
        f[b - 1] += 1

count = collections.Counter(uf.par)
# print(uf.par)
# print(count)
# print(f)
for i in range(n):
    print(count[uf.par[i]] - f[i] - 1, "", end="")
print()
