from collections import deque

class EDOMONDS_KARP():
    def __init__(self, N, s, t):
        self.N = N; self.s = s; self.t = t
        self.cap = [[0]*N for _ in range(N)]
        self.link = [[] for _ in range(N)]

    def add_edge(self, u, v, c):
        self.cap[u][v] = c
        self.link[u].append(v)
        self.link[v].append(u)

    def max_flow(self):
        N = self.N; s = self.s; t = self.t
        f = 0
        flow = [[0]*N for _ in range(N)]
        while True:
            m, prev = self.bfs(flow)
            if m == 0:
                break
            f += m
            v = t
            while v != s:
                u = prev[v]
                flow[u][v] += m
                flow[v][u] -=m
                v = u
        return (f, flow)

    def bfs(self, flow):
        N = self.N; s = self.s; t = self.t
        cap = self.cap
        link = self.link
        prev = [-1]*N; prev[s] = -2
        m = [0]*N; m[s] = float('inf')
        q = deque([s])
        while q:
            u = q.popleft()
            for v in link[u]:
                if cap[u][v] - flow[u][v] > 0 and prev[v] == -1:
                    prev[v] = u
                    m[v] = min(m[u], cap[u][v] - flow[u][v])
                    if v != t:
                        q.append(v)
                    else:
                        return (m[t], prev)
        return (0, prev)

H, W = list(map(int, input().split()))
board = [input() for _ in range(H)]

EK = EDOMONDS_KARP(H + W + 2, 0, H + W + 1)
for h in range(H):
    for w in range(W):
        if board[h][w] == 'o':
            EK.add_edge(h + 1, w + H + 1, 1)
            EK.add_edge(w + H + 1, h + 1, 1)
        if board[h][w] == 'S':
            EK.add_edge(0, h + 1, float('inf'))
            EK.add_edge(0, w + H + 1, float('inf'))
        if board[h][w] == 'T':
            EK.add_edge(h + 1, H + W + 1, float('inf'))
            EK.add_edge(w + H + 1, H + W + 1, float('inf'))

f, _ = EK.max_flow()
print((f if f < float('inf') else -1))

