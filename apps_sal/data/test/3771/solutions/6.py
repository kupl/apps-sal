from collections import deque
INF = float("inf")
TO = 0; CAP = 1; REV = 2


class Dinic:
    def __init__(self, N):
        self.N = N
        self.V = [[] for _ in range(N)]  # to, cap, rev
        # 辺 e = V[n][m] の逆辺は V[e[TO]][e[REV]]
        self.level = [0] * N

    def add_edge(self, u, v, cap):
        self.V[u].append([v, cap, len(self.V[v])])
        self.V[v].append([u, 0, len(self.V[u]) - 1])

    def add_edge_undirected(self, u, v, cap):  # 未検証
        self.V[u].append([v, cap, len(self.V[v])])
        self.V[v].append([u, cap, len(self.V[u]) - 1])

    def bfs(self, s: int) -> bool:
        self.level = [-1] * self.N
        self.level[s] = 0
        q = deque()
        q.append(s)
        while len(q) != 0:
            v = q.popleft()
            for e in self.V[v]:
                if e[CAP] > 0 and self.level[e[TO]] == -1:  # capが1以上で未探索の辺
                    self.level[e[TO]] = self.level[v] + 1
                    q.append(e[TO])
        return True if self.level[self.g] != -1 else False  # 到達可能

    def dfs(self, v: int, f) -> int:
        if v == self.g:
            return f
        for i in range(self.ite[v], len(self.V[v])):
            self.ite[v] = i
            e = self.V[v][i]
            if e[CAP] > 0 and self.level[v] < self.level[e[TO]]:
                d = self.dfs(e[TO], min(f, e[CAP]))
                if d > 0:  # 増加路
                    e[CAP] -= d  # cap を減らす
                    self.V[e[TO]][e[REV]][CAP] += d  # 反対方向の cap を増やす
                    return d
        return 0

    def solve(self, s, g):
        self.g = g
        flow = 0
        while self.bfs(s):  # 到達可能な間
            self.ite = [0] * self.N
            f = self.dfs(s, INF)
            while f > 0:
                flow += f
                f = self.dfs(s, INF)
        return flow


H, W = list(map(int, input().split()))
dinic = Dinic(H + W + 2)
for i in range(H):
    a = input()
    for j, a_ in enumerate(a):
        if a_ == "S":
            start = i, j
        elif a_ == "T":
            goal = i, j
        if a_ != ".":
            dinic.add_edge_undirected(H + j, i, 1)
dinic.add_edge_undirected(H + W, start[0], 1 << 30)
dinic.add_edge_undirected(H + W, start[1] + H, 1 << 30)
dinic.add_edge_undirected(H + W + 1, goal[0], 1 << 30)
dinic.add_edge_undirected(H + W + 1, goal[1] + H, 1 << 30)

if start[0] == goal[0] or start[1] == goal[1]:
    print((-1))
else:
    print((dinic.solve(H + W, H + W + 1)))
