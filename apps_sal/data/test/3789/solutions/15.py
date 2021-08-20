from collections import deque
INF = 10 ** 30


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
            for (w, cap, _) in g[v]:
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
        g = self.g
        while self.bfs(s, t):
            (*self.it,) = map(iter, self.g)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


n = int(input())
a = [-1] + list(map(int, input().split()))
d = Dinic(n + 2)
(s, t) = (0, n + 1)
for i in range(1, n + 1):
    if a[i] > 0:
        d.add_edge(i, t, a[i])
    elif a[i] < 0:
        d.add_edge(s, i, -a[i])
    for j in range(2 * i, n + 1, i):
        d.add_edge(i, j, INF)
res = d.flow(s, t)
print(sum([x for x in a if x > 0]) - res)
