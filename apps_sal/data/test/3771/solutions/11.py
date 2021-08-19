import sys
input = sys.stdin.readline
(H, W) = list(map(int, input().split()))
a = [list(input())[:-1] for _ in range(H)]
c = H + W - 1


class FordFulkerson:

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

    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            (w, cap, rev) = e
            if cap and (not used[w]):
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        f = INF = c
        N = self.N
        while f:
            self.used = [0] * N
            f = self.dfs(s, t, INF)
            flow += f
        return flow


flk = FordFulkerson(H * W * 2 + H + W + 1)
b = H * W
s = 0
t = 0
for i in range(H):
    for j in range(W):
        if a[i][j] != '.':
            flk.add_edge(b + i * W + j, b * 2 + i, c)
            flk.add_edge(b * 2 + i, i * W + j, c)
for j in range(W):
    for i in range(H):
        if a[i][j] != '.':
            flk.add_edge(b + i * W + j, b * 2 + H + j, c)
            flk.add_edge(b * 2 + H + j, i * W + j, c)
for i in range(H):
    for j in range(W):
        if a[i][j] != '.':
            flk.add_edge(i * W + j, b + i * W + j, 1)
        if a[i][j] == 'S':
            s = b + i * W + j
        if a[i][j] == 'T':
            t = i * W + j
if (s - b) % W != t % W and (s - b) // W != t // W:
    if sum([x.count('o') for x in a]) == H * W - 2:
        print(min(H, W) * 2 - 2)
    else:
        print(flk.flow(s, t))
else:
    print(-1)
