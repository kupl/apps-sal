INF = float('inf')
INF = 2 << 30


class Dinic:

    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])

    def dfs(self, v, t, f):
        if v == t or not f:
            return f
        for i in range(self.ptr[v], len(self.adj[v])):
            e = self.adj[v][i]
            if self.lvl[e[0]] == self.lvl[v] + 1:
                p = self.dfs(e[0], t, min(f, e[2] - e[3]))
                if p:
                    self.adj[v][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[v] += 1
        return 0

    def calc(self, s, t):
        (flow, self.q[0]) = (0, s)
        for l in range(31):
            while True:
                (self.lvl, self.ptr) = ([0] * len(self.q), [0] * len(self.q))
                (qi, qe, self.lvl[s]) = (0, 1, 1)
                while qi < qe and (not self.lvl[t]):
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and e[2] - e[3] >> 30 - l:
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1
                p = self.dfs(s, t, INF)
                while p:
                    flow += p
                    p = self.dfs(s, t, INF)
                if not self.lvl[t]:
                    break
        return flow


(n, m) = list(map(int, input().split()))
s = 2 * n
t = 2 * n + 1
MF = Dinic(2 * n + 2)
out = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(n):
    a = A[i]
    v = B[i]
    out += a
    MF.add_edge(i, i + n, INF)
    if a - v > 0:
        MF.add_edge(s, i, a - v)
    else:
        out += v - a
    if a + v > 0:
        MF.add_edge(i + n, t, a + v)
    else:
        out -= v + a
for i in range(m):
    (u, v) = list(map(int, input().split()))
    MF.add_edge(u - 1, v - 1 + n, INF)
    MF.add_edge(v - 1, u - 1 + n, INF)
print(out - MF.calc(s, t))
