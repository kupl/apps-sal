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
            for (w, cap, _) in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            (w, cap, rev) = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10 ** 18
        G = self.G
        while self.bfs(s, t):
            (*self.it,) = list(map(iter, self.G))
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


(N,) = list(map(int, input().split()))
(a, b, c) = list(map(int, input().split()))
(x, y, z) = list(map(int, input().split()))
INF = 10 ** 9
dnc = Dinic(8)
dnc.add_edge(0, 1, a)
dnc.add_edge(0, 2, b)
dnc.add_edge(0, 3, c)
dnc.add_edge(1, 4, INF)
dnc.add_edge(2, 5, INF)
dnc.add_edge(3, 6, INF)
dnc.add_edge(1, 6, INF)
dnc.add_edge(2, 4, INF)
dnc.add_edge(3, 5, INF)
dnc.add_edge(4, 7, x)
dnc.add_edge(5, 7, y)
dnc.add_edge(6, 7, z)
print(N - dnc.flow(0, 7), min(a, y) + min(b, z) + min(c, x))
