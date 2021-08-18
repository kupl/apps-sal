import sys
import bisect
import math
import itertools
import string
import queue
import copy
import heapq
import collections
import itertools
sys.setrecursionlimit(10**8)
mod = 998244353
def inp(): return int(input())
def inpm(): return list(map(int, input().split()))
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplt(n): return [tuple(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, k = inpm()
A = inpll(n)

uf_r = UnionFind(n)
uf_c = UnionFind(n)
for i in range(n):
    for j in range(i + 1, n):
        flg = True
        for l in range(n):
            if A[i][l] + A[j][l] > k:
                flg = False
                break
        if flg:
            uf_c.union(i, j)

        flg = True
        for l in range(n):
            if A[l][i] + A[l][j] > k:
                flg = False
                break
        if flg:
            uf_r.union(i, j)

ans = 1
for i in uf_c.roots():
    ans = (ans * math.factorial(uf_c.parents[i] * -1)) % mod
for i in uf_r.roots():
    ans = (ans * math.factorial(uf_r.parents[i] * -1)) % mod

print(ans)
