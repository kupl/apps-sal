
import sys
from collections import deque


class Dinic:
    def __init__(self, N, inf):
        self.N = N
        self.inf = inf
        self.G = [[] for _ in range(N)]
        self.level = [0] * N

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

    def bfs(self, s):
        self.level = [-1] * self.N
        deq = deque([s])
        self.level[s] = 0
        while deq:
            v = deq.pop()
            lv = self.level[v] + 1
            for w, cap, _ in self.G[v]:
                if cap > 0 and self.level[w] == -1:
                    self.level[w] = lv
                    deq.appendleft(w)

    def dfs(self, v, t, f):
        if v == t:
            return f
        for e in self.iter[v]:
            w, cap, rev = e
            if cap > 0 and self.level[v] < self.level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d > 0:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] == -1:
                return flow
            *self.iter, = list(map(iter, self.G))
            f = self.inf
            while f > 0:
                f = self.dfs(s, t, self.inf)
                flow += f


sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり


N = I()
A = [0] + LI()
ans = sum(A[i] for i in range(1, N + 1) if A[i] > 0)

inf = 10**18
Di = Dinic(N + 2, inf)
s, t = 0, N + 1

for i in range(1, N + 1):
    Di.add_edge(s, i, max(0, -A[i]))
    Di.add_edge(i, t, max(0, A[i]))

for i in range(1, N // 2 + 1):
    for j in range(2 * i, N + 1, i):
        Di.add_edge(i, j, inf)

print((ans - Di.flow(s, t)))
