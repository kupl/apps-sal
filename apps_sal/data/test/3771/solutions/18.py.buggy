import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce


def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


class Dinic:
    def __init__(self, v, inf=10**10):
        self.v = v
        self.inf = inf
        self.G = [[] for _ in range(v)]
        self.level = [-1] * v  # 深さ
        self.ite = [0] * v  # DFSでの探索が済んでいるか

    def add_edge(self, fr, to, cap):
        self.G[fr].append([to, cap, len(self.G[to])])
        self.G[to].append([fr, 0, len(self.G[fr]) - 1])

    def bfs(self, s):  # BFSで深さ決定,sがstart
        self.level = [-1] * self.v  # 必要
        self.level[s] = 0
        Q = deque()
        Q.append(s)
        while Q:
            v = Q.popleft()
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if e[1] > 0 and self.level[e[0]] < 0:  # capacity>0かつtoの深さ未定
                    self.level[e[0]] = self.level[v] + 1
                    Q.append(e[0])

    def dfs(self, v, t, f):  # DFSで増加パス探索,v開始、t終点、総フローf
        if v == t:
            return f
        for i in range(self.ite[v], len(self.G[v])):
            self.ite[v] = i
            e = self.G[v][i]
            if e[1] > 0 and self.level[v] < self.level[e[0]]:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d > 0:
                    e[1] -= d  # cap減少
                    self.G[e[0]][e[2]][1] += d  # 逆辺のcap増加
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.ite = [0] * self.v  # DFSでの探索が済んでいるか否か
            f = self.dfs(s, t, self.inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.inf)


H, W = MAP()
a = [list(input()) for _ in range(H)]
D = Dinic(H + W + 2)

for i in range(H):
    for j in range(W):
        if a[i][j] == "S":
            sy, sx = i, j
            D.add_edge(0, i + 1, INF)
            D.add_edge(0, H + j + 1, INF)
        elif a[i][j] == "T":
            gy, gx = i, j
            D.add_edge(i + 1, H + W + 1, INF)
            D.add_edge(H + j + 1, H + W + 1, INF)
        elif a[i][j] == "o":
            D.add_edge(i + 1, H + j + 1, 1)
            D.add_edge(H + j + 1, i + 1, 1)

if sy == gy or sx == gx:
    print((-1))
    return

print((D.max_flow(0, H + W + 1)))
