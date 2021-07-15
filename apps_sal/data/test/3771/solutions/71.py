import collections
import queue


class Dinic:
    def __init__(self, N):
        self.N = N
        self.edges = collections.defaultdict(list)
        self.level = [0 for _ in range(self.N)]
        self.iter = [0 for _ in range(self.N)]

    def add(self, u, v, c, directed=True):
        if directed:
            self.edges[u].append([v, c, len(self.edges[v])])
            self.edges[v].append([u, 0, len(self.edges[u])-1])
        else:  # TODO: must be Verified
            self.edges[u].append([v, c, len(self.edges[v])])
            self.edges[v].append([u, 0, len(self.edges[u]) - 1])
            self.edges[v].append([u, c, len(self.edges[u])])
            self.edges[u].append([v, 0, len(self.edges[v]) - 1])

    def bfs(self, s):
        self.level = [-1 for _ in range(self.N)]
        self.level[s] = 0
        que = queue.Queue()
        que.put(s)
        while not que.empty():
            v = que.get()
            for i in range(len(self.edges[v])):
                e = self.edges[v][i]
                if e[1] > 0 and self.level[e[0]] < 0:
                    self.level[e[0]] = self.level[v] + 1
                    que.put(e[0])

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.edges[v])):
            self.iter[v] = i
            e = self.edges[v][i]
            if e[1] > 0 and self.level[v] < self.level[e[0]]:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d > 0:
                    e[1] -= d
                    self.edges[e[0]][e[2]][1] += d
                    return d
        return 0

    def maxFlow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0 for _ in range(self.N)]
            f = self.dfs(s, t, float('inf'))
            while f > 0:
                flow += f
                f = self.dfs(s, t, float('inf'))


H, W = map(int, input().split())
graph = Dinic(H+W+2)

for h in range(H):
    tmp = str(input())
    for w in range(W):
        if tmp[w] == 'o':
            graph.add(h+1, H+1+w, 1)
            graph.add(H + w + 1, h + 1, 1)
        if tmp[w] == 'S':
            start = [h, w]
            graph.add(0, h+1, float('inf'))
            graph.add(0, H+w+1, float('inf'))
        if tmp[w] == 'T':
            goal = [h, w]
            graph.add(h+1, H+W+1, float('inf'))
            graph.add(H+1+w, H+W+1, float('inf'))

if start[0] == goal[0] or start[1] == goal[1]:
    print(-1)
    return
print(graph.maxFlow(0, H+W+1))
