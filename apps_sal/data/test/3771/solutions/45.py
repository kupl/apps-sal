from collections import deque
from itertools import combinations


class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[]for _ in range(N)]

    def add_edge(self, fr, to, cap):
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
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


INF = 10**9 + 7
t, *a = open(0)
h, w = map(int, t.split())
d = Dinic(h + w + 3)
add = d.add_multi_edge
for i, s in enumerate(a, 1):
    for j, t in enumerate(s[:-1], h + 1):
        if t != '.':
            if t == 'S':
                add(0, i, INF, INF)
                add(0, j, INF, INF)
            elif t == 'T':
                add(i, h + w + 2, INF, INF)
                add(j, h + w + 2, INF, INF)
            add(i, j, 1, 1)
a = d.flow(0, h + w + 2)
print(-(a >= INF) or a)
