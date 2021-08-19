from collections import defaultdict
import sys
import itertools
import time
import math
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
(N, M) = map(int, input().split())


class UnionFind(object):

    def __init__(self, n=1):
        self.link = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.link[x] == x:
            return x
        self.link[x] = self.find(self.link[x])
        return self.link[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            (x, y) = (y, x)
        self.link[y] = x
        self.size[x] += self.size[y]

    def get_size(self, x):
        x = self.find(x)
        return self.size[x]


es = [0] * M
for i in range(M):
    (a, b) = map(int, input().split())
    es[i] = (a - 1, b - 1)
u = UnionFind(N)
ans = []
pair = N * (N - 1) // 2
ans.append(pair)
for i in range(M - 1, -1, -1):
    (a, b) = es[i]
    if u.is_same(a, b):
        ans.append(pair)
        continue
    pair -= u.get_size(a) * u.get_size(b)
    u.unite(a, b)
    if pair < 0:
        pair = 0
    ans.append(pair)
for i in list(reversed(ans))[1:]:
    print(i)
