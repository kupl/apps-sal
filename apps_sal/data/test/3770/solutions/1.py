# Dinic's algorithm
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
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
edge = [tuple(map(int,input().split())) for i in range(M)]

G = Dinic(2*N+2)
res = 0
for i in range(1,N+1):
    if B[i-1]>0:
        res += B[i-1]
        G.add_edge(0,i,B[i-1])
        G.add_edge(0,N+i,B[i-1])
        G.add_edge(N+i,i,A[i-1])
    else:
        G.add_edge(i,2*N+1,-B[i-1])
        res += -B[i-1]
        G.add_edge(N+i,2*N+1,-B[i-1])
        G.add_edge(N+i,i,A[i-1])
    G.add_edge(i,N+i,10**15)

for u,v in edge:
    G.add_edge(u,N+v,10**15)
    G.add_edge(v,N+u,10**15)

res -= G.flow(0,2*N+1)

print(res)
