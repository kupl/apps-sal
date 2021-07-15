#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

class DisjointSet:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.rank = [0] * n
        self.max_member = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def has_same_root(self, x, y):
        return self.root(x) == self.root(y)

    def get_size(self, x):
        return self.size[self.root(x)]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.max_member[y] = max(self.max_member[x], self.max_member[y])
        else:
            self.par[y] = x
            self.max_member[x] = max(self.max_member[x], self.max_member[y])
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

n, m = [int(item) for item in input().split()]
DS = DisjointSet(n)
for i in range(m):
    u, v = [int(item) - 1 for item in input().split()]
    DS.unite(u, v)
goal = 0
par = 0
ans = 0
for i in range(n):
    if goal <= i:
        par = DS.par[i]
        goal = DS.max_member[par]
        continue
    if DS.has_same_root(par, i): 
        continue
    else:
        DS.unite(par, i)
        ans += 1
        par = DS.par[i]
        goal = DS.max_member[par]
print(ans)
