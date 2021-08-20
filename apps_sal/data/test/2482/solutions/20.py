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
        self._size = [1 for _ in range(n)]

    def unite(self, x: int, y: int) -> None:
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self._link(px, py)

    def _link(self, x: int, y: int):
        if self._size[x] < self._size[y]:
            self._parents[x] = y
            self._size[y] += self._size[x]
        else:
            self._parents[y] = x
            self._size[x] += self._size[y]

    def same(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        return px == py

    def find(self, x: int) -> int:
        if self._parents[x] == x:
            return x
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def size(self, x: int):
        return self._size[self.find(self._parents[x])]


(N, K, L) = map(int, input().split())
road = UnionFind(N + 1)
rail = UnionFind(N + 1)
share = UnionFind(N + 1)
roads = [list(map(int, input().split())) for _ in range(K)]
rails = [list(map(int, input().split())) for _ in range(L)]
for i in range(K):
    (p, q) = roads[i]
    road.unite(p, q)
for i in range(L):
    (r, s) = rails[i]
    rail.unite(r, s)
m = {}
for i in range(1, N + 1):
    cnt = m.get((road.find(i), rail.find(i)), 0)
    m[road.find(i), rail.find(i)] = cnt + 1
ans = [0] * N
for i in range(N):
    ans[i] = m[road.find(i + 1), rail.find(i + 1)]
print(*ans)
