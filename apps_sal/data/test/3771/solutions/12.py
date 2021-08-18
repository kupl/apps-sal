from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in range(n)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.g[fr].append(forward)
        self.g[to].append(backward)

    def add_bidirectional_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.g[v1].append(edge1)
        self.g[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None] * self.n
        deq = deque([s])
        level[s] = 0
        g = self.g
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in g[v]:
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
        INF = 10**30
        g = self.g
        while self.bfs(s, t):
            *self.it, = map(iter, self.g)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


H, W = map(int, input().split())
a = [input() for _ in range(H)]
d = Dinic(H + W + 2)
for i in range(H):
    for j in range(W):
        if a[i][j] == "S":
            d.add_edge(H + W, i, 10**5)
            d.add_edge(H + W, H + j, 10**5)
        elif a[i][j] == "T":
            d.add_edge(i, H + W + 1, 10**5)
            d.add_edge(H + j, H + W + 1, 10**5)
        elif a[i][j] == "o":
            d.add_edge(i, H + j, 1)
            d.add_edge(H + j, i, 1)
ans = d.flow(H + W, H + W + 1)
if ans > 10000:
    print(-1)
else:
    print(ans)
