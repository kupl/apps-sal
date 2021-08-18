import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy


class UnionFind:

    def __init__(self, n: int):
        self._n = n
        self._parents = [i for i in range(n)]
        self._rank = [1 for _ in range(n)]

    def unite(self, x: int, y: int) -> None:
        px = self.find(x)
        py = self.find(y)

        if px != py:
            self._link(px, py)

    def _link(self, x: int, y: int):
        if self._rank[x] < self._rank[y]:
            self._parents[x] = y
        elif self._rank[x] > self._rank[y]:
            self._parents[y] = x
        else:
            self._parents[x] = y
            self._rank[y] += 1

    def same(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        return px == py

    def find(self, x: int) -> int:
        if self._parents[x] == x:
            return x

        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]


N = int(input())
ps = [list(map(int, input().split())) + [i] for i in range(N)]
ps.sort(key=lambda t: t[0])
xs = []
for i in range(N - 1):
    xs.append((ps[i + 1][0] - ps[i][0], ps[i][2], ps[i + 1][2]))

ps.sort(key=lambda t: t[1])
ys = []
for i in range(N - 1):
    ys.append((ps[i + 1][1] - ps[i][1], ps[i][2], ps[i + 1][2]))

xs += [(1 << 40, -1, -1)]
ys += [(1 << 40, -1, -1)]

xs.sort()
ys.sort()

xc, yc = 0, 0
uf = UnionFind(N)

ans = 0
while xc < N - 1 and yc < N - 1:
    if xs[xc][0] < ys[yc][0]:
        if not uf.same(xs[xc][1], xs[xc][2]):
            uf.unite(xs[xc][1], xs[xc][2])
            ans += xs[xc][0]
        xc += 1
    else:
        if not uf.same(ys[yc][1], ys[yc][2]):
            uf.unite(ys[yc][1], ys[yc][2])
            ans += ys[yc][0]
        yc += 1

print(ans)
