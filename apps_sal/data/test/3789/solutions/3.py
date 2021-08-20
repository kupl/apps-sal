N = int(input())
alist = [0] + list(map(int, input().split()))
xlist = list(range(1, N + 1))


class FordFulkerson:

    def __init__(self, vlist):
        self.G = {}
        for v in vlist:
            self.G[v] = []

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
        used[v] = True
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
        f = INF = 10 ** 9 + 7
        while f:
            self.used = {}
            for v in self.G:
                self.used[v] = False
            f = self.dfs(s, t, INF)
            flow += f
        return flow


asum_pos = 0
ff = FordFulkerson(range(N + 2))
for i in range(1, N + 1):
    a = alist[i]
    if a <= 0:
        ff.add_edge(0, i, -a)
    else:
        ff.add_edge(i, N + 1, a)
        asum_pos += a
for i in range(1, N + 1):
    for j in range(2 * i, N + 1, i):
        ff.add_edge(i, j, float('inf'))
penalty = ff.flow(0, N + 1)
print(asum_pos - penalty)
