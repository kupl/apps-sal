import queue


class Dinic:
    """Implementation of Dinic's Alogorithm"""

    def __init__(self, v, inf=1000000007):
        self.V = v
        self.inf = inf
        self.G = [[] for _ in range(v)]
        self.level = [0 for _ in range(v)]
        self.iter = [0 for _ in range(v)]

    def add_edge(self, from_, to, cap):
        self.G[from_].append({'to': to, 'cap': cap, 'rev': len(self.G[to])})
        self.G[to].append({'to': from_, 'cap': 0, 'rev': len(self.G[from_]) - 1})

    def bfs(self, s):
        self.level = [-1 for _ in range(self.V)]
        self.level[s] = 0
        que = queue.Queue()
        que.put(s)
        while not que.empty():
            v = que.get()
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1
                    que.put(e['to'])

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i
            e = self.G[v][i]
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
                d = self.dfs(e['to'], t, min(f, e['cap']))
                if d > 0:
                    e['cap'] -= d
                    self.G[e['to']][e['rev']]['cap'] += d
                    return d

        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0 for _ in range(self.V)]
            f = self.dfs(s, t, self.inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.inf)


def __starting_point():
    H, W = list(map(int, input().split()))
    a = [list(input()) for i in range(H)]
    Dn = Dinic(2 + H + W)
    INF = 10**15
    s = (-1, -1)
    t = (-1, -1)
    for i in range(H):
        for j in range(W):
            if a[i][j] != ".":
                Dn.add_edge(i + 1, H + 1 + j, 1)
                Dn.add_edge(H + 1 + j, i + 1, 1)
            if a[i][j] == "S":
                Dn.add_edge(0, i + 1, INF)
                Dn.add_edge(0, H + 1 + j, INF)
                s = (i, j)
            if a[i][j] == "T":
                Dn.add_edge(i + 1, H + W + 1, INF)
                Dn.add_edge(H + 1 + j, H + W + 1, INF)
                t = (i, j)
    if s[0] == t[0] or s[1] == t[1]:
        print((-1))
    else:
        ans = Dn.max_flow(0, 1 + H + W)
        print(ans)


__starting_point()
