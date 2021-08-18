from decimal import ROUND_HALF_UP, Decimal
from collections import deque, Counter, defaultdict
from collections import deque
from bisect import bisect_left as bileft, bisect_right as biright
from functools import lru_cache
from math import sqrt, ceil
import sys
mod = 10**9 + 7
inf = float("inf")
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)


class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap=1):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None] * self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = inf
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


n = int(input())
dinic = Dinic(2 * n + 2)


A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append([a, b])
for i in range(n):
    a, b = map(int, input().split())
    B.append([a, b])
for i in range(n):
    dinic.add_edge(2 * n, i, 1)
    dinic.add_edge(i + n, 2 * n + 1, 1)
for i in range(n):
    for j in range(n):
        if A[i][0] < B[j][0] and A[i][1] < B[j][1]:
            dinic.add_edge(i, j + n)

print(dinic.flow(2 * n, 2 * n + 1))
