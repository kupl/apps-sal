# Dinic's algorithm
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]#(行き先、容量、逆辺の参照)
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
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
        INF = 10**10
        G = self.G
        while self.bfs(s, t):
            *self.it, = list(map(iter, self.G))
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow
inf = 10**9
H, W = list(map(int, input().split()))
a = [list(input()) for _ in range(H)]
D = Dinic(H+W+2)
for i in range(H):
    for j in range(W):
        if a[i][j] == 'S':
            D.add_edge(0, i+1, inf)
            D.add_edge(0, j+1+H, inf)
        elif a[i][j] == 'T':
            D.add_edge(i+1, H+W+1, inf)
            D.add_edge(j+1+H, H+W+1, inf)
        elif a[i][j] == 'o':
            D.add_edge(i+1, j+1+H, 1)
            D.add_edge(j+1+H, i+1, 1)
ans = D.flow(0, H+W+1)
print((ans if ans<inf else -1))






