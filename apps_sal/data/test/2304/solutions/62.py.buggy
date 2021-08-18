#!/usr/bin/env python3
class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.weight = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            px = self.find(self.parents[x])
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = px
            return px

    def union(self, x, y, w):
        w += self.weight[x] - self.weight[y]
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y, w = y, x, -w
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.weight[y] = w
        return

    def weig(self, x):
        self.find(x)
        return self.weight[x]

    def diff(self, x, y):
        return self.weig(y) - self.weig(x)

    def same(self, x, y):
        return self.find(x) == self.find(y)


(n, m), *q = [[*map(int, o.split())] for o in open(0)]
UF = WeightedUnionFind(n + 1)
for l, r, d in q:
    if UF.same(l, r):
        if d != abs(UF.diff(l, r)):
            print("No")
            return
    else:
        UF.union(l, r, d)
print("Yes")
