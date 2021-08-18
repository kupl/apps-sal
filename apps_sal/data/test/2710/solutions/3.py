
class Dinic:
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

        def __repr__(self):
            return "(to: {0} cap: {1} rev: {2})".format(self.to, self.cap, self. rev)

    def __init__(self, V):
        self.V = V
        self.size = [0 for i in range(V)]
        self.G = [[] for i in range(V)]

    def add_edge(self, _from, to, cap):
        self.G[_from].append(self.Edge(to, cap, self.size[to]))
        self.G[to].append(self.Edge(_from, 0, self.size[_from]))
        self.size[_from] += 1
        self.size[to] += 1

    def bfs(self, s):
        level = [-1 for i in range(self.V)]
        level[s] = 0
        q = []
        q.append(s)
        while q != []:
            v = q.pop(0)
            for u in self.G[v]:
                if u.cap > 0 and level[u.to] < 0:
                    level[u.to] = level[v] + 1
                    q.append(u.to)
        return level

    def dfs(self, v, t, f):
        if v == t:
            return f
        while self.iterator[v] < self.size[v]:
            edge = self.G[v][self.iterator[v]]
            if edge.cap > 0 and self.level[v] < self.level[edge.to]:
                d = self.dfs(edge.to, t, f if f < edge.cap else edge.cap)
                if d > 0:
                    self.G[v][self.iterator[v]].cap -= d
                    self.G[edge.to][edge.rev].cap += d
                    return d
            self.iterator[v] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.level = self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iterator = [0 for i in range(self.V)]
            while True:
                f = self.dfs(s, t, float('inf'))
                if f == 0:
                    break
                flow += f


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ff = Dinic(N * 2 + 2)
S = 1
T = N + 1

for i in range(M):
    p, q = list(map(int, input().split()))
    ff.add_edge(p, T + q - 1, 10**9)
    ff.add_edge(q, T + p - 1, 10**9)

for i in range(N):
    ff.add_edge(i + 1, T + i, 10**9)
    ff.add_edge(0, S + i, A[i])
    ff.add_edge(T + i, 2 * N + 1, B[i])

ans = [[0 for i in range(N)] for j in range(N)]
ff.max_flow(0, 2 * N + 1)

for i in range(1, N + 1):
    for v in ff.G[i]:
        if v.to != 0:
            ans[i - 1][v.to - T] = ff.G[v.to][v.rev].cap

if sum(A) != sum(B):
    print('NO')
    quit()
if [sum([ans[i][j] for i in range(N)]) for j in range(N)] == B:
    print('YES')
    for a in ans:
        print(' '.join(map(str, a)))
else:
    print('NO')
