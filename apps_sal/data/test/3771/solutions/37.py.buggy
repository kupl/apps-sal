from collections import deque


class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

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


h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

sa = Dinic(h + w + 2)
INF = 10**9 + 7
s = 0
t = h + w + 1
for i in range(h):
    for j in range(w):
        if a[i][j] == "S":
            sa.add_edge(s, i + 1, INF)
            sa.add_edge(s, h + 1 + j, INF)
        if a[i][j] == "T":
            sa.add_edge(i + 1, t, INF)
            sa.add_edge(h + 1 + j, t, INF)
        if a[i][j] != ".":
            sa.add_edge(i + 1, h + 1 + j, 1)
            sa.add_edge(h + 1 + j, i + 1, 1)

if sa.flow(s, t) > h * w:
    print(-1)
    return
print(sa.flow(t, s))
