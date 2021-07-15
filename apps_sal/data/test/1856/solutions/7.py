#!/usr/bin/env python3
import sys
input = sys.stdin.readline

class DisjointSet:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.rank = [0] * n

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

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

n = int(input())
password = []
DS = DisjointSet(26)
seen = set()
orda = ord("a")
for i in range(n):
    password = input().rstrip()
    if len(password) == 1:
        seen.add(password)
        continue
    for ch1, ch2 in zip(password, password[1:]):
        DS.unite(ord(ch1) - orda, ord(ch2) - orda)
        seen.add(ch1)
        seen.add(ch2)
pars = set()
for item in seen:
    pars.add(DS.root(ord(item) - orda))
print(len(pars))
