from collections import deque


class Dinic:
    def __init__(self, v, inf=10**9 + 7):
        self.V = v
        self.inf = inf
        self.G = [list() for _ in range(v)]
        self.level = [-1 for _ in range(v)]
        self.iter = [0] * v

    def addedge(self, fr, to, cap):
        """
        G[fr] = [to, cap, rev]
        """
        go = [to, cap, None]
        go[2] = back = [fr, 0, go]
        self.G[fr].append(go)
        self.G[to].append(back)

    def bfs(self, st, en):
        q = deque([st])
        self.level = [-1 for _ in range(self.V)]
        self.level[st] = 0
        while q:
            cur = q.popleft()
            for x, cap, _ in self.G[cur]:
                if cap and self.level[x] < 0:
                    self.level[x] = self.level[cur] + 1
                    q.append(x)
        return self.level[en] > 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        for e in self.iter[v]:
            w, cap, rev = e
            if cap and self.level[v] < self.level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.iter = list(map(iter, self.G))
            f = self.dfs(s, t, self.inf)
            while f:
                flow += f
                f = self.dfs(s, t, self.inf)
        return flow


H, W = map(int, input().split())
dinic = Dinic(200)
for y in range(H):
    s = input()
    for x in range(W):
        if s[x] == 'o':
            dinic.addedge(y, x + 100, 1)
            dinic.addedge(x + 100, y, 1)
        elif s[x] == 'S':
            sy, sx = y, x
            dinic.addedge(y, x + 100, 10**5)
            dinic.addedge(x + 100, y, 10**5)
        elif s[x] == 'T':
            ty, tx = y, x
            dinic.addedge(y, x + 100, 10**5)
            dinic.addedge(x + 100, y, 10**5)
print(-1 if sy == ty or sx == tx else dinic.flow(sy, ty))
