from sys import setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *


def read():
    return int(input())


def reads():
    return [int(x) for x in input().split()]


INF = 1 << 60


def main():
    N = read()
    A = reads()
    offset = sum(a for a in A if a > 0)
    di = dinic(N + 2)  # 0: source, N+1: target
    for i in range(1, N + 1):
        a = A[i - 1]
        if a <= 0:
            di.add_edge(0, i, -a)
        else:
            di.add_edge(i, N + 1, a)
        for j in range(2 * i, N + 1, i):
            di.add_edge(i, j, INF)
    ans = offset - di.max_flow(0, N + 1)
    print(ans)


class dinic:
    def __init__(self, N): self.size = N; self.edges = [[] for _ in range(N)]
    def add_edge(self, u, v, c): self.edges[u].append((v, c)); self.edges[v].append((u, 0))

    def bfs(self, cap, s):
        N = self.size; edges = self.edges
        level = [-1] * N; level[s] = 0
        que = deque([s])
        while len(que) > 0:
            u = que.popleft()
            for v, _ in edges[u]:
                if cap[u][v] > 0 and level[v] < 0: level[v] = level[u] + 1; que.append(v)
        return level

    def dfs(self, cap, itr, level, u, t, f):
        N = self.size; edges = self.edges
        if u == t: return f
        for i in range(itr[u], len(edges[u])):
            itr[u] = i
            v, _ = edges[u][i]
            if cap[u][v] > 0 and level[u] < level[v]:
                d = self.dfs(cap, itr, level, v, t, min(f, cap[u][v]))
                if d > 0: cap[u][v] -= d; cap[v][u] += d; return d
        return 0

    def max_flow(self, s, t):
        N = self.size; edges = self.edges; cap = [[0] * N for _ in range(N)]
        for u in range(N):
            for v, c in edges[u]: cap[u][v] += c
        flow = 0
        while True:
            level = self.bfs(cap, s)
            if level[t] < 0: return flow
            itr = [0] * N
            while True:
                f = self.dfs(cap, itr, level, s, t, INF)
                if f <= 0: break
                flow += f


main()
