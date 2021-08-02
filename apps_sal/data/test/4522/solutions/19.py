# -*- coding: utf-8 -*-

import sys
from itertools import accumulate
from operator import itemgetter


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


INF = 10 ** 18
MOD = 10 ** 9 + 7


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.tree = [True] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            self.tree[x] = False
            return
        if not self.tree[x] or not self.tree[y]:
            self.tree[x] = self.tree[y] = False

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x=None):
        if x is not None:
            return self.size[self.find(x)]
        else:
            res = set()
            for i in range(self.n + 1):
                res.add(self.find(i))
            return len(res) - 1

    def is_tree(self, x):
        return self.tree[self.find(x)]


N, M = MAP()
edges = []
for i in range(N - 1):
    a, b, c = MAP()
    a -= 1
    b -= 1
    edges.append((c, a, b))

if N == 1:
    LIST()
    ans = [0] * M
    print(*ans)
    return

MAX = 2 * 10**5 + 7
edges.sort(key=itemgetter(0))
C = [0] * MAX
uf = UnionFind(N)
prevc = edges[0][0]
for c, a, b in edges:
    if prevc != c:
        C[c] = C[prevc]
    sz1 = uf.get_size(a)
    C[c] -= sz1 * (sz1 - 1) // 2
    sz2 = uf.get_size(b)
    C[c] -= sz2 * (sz2 - 1) // 2
    uf.union(a, b)
    sz = sz1 + sz2
    C[c] += sz * (sz - 1) // 2
    prevc = c

C = list(accumulate(C, max))
Q = LIST()
ans = [0] * M
for i, q in enumerate(Q):
    ans[i] = C[q]
print(*ans)
