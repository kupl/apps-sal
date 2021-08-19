# graph = [{} for _ in range(V)]
# when there is an edge u -> v (maxflow f)
#  graph[u][v] = f
#  graph[v][u] = f (if undirected) 0 (if directed)

import sys


class FordFulkerson():
    def __init__(self, start, finish, graph, INF=10**18):
        self.INF = INF
        self.start = start
        self.finish = finish
        self.graph = graph
        self.N = len(graph)

    def dfs(self):
        self.Flow = [self.INF] * self.N
        self.used = [False] * self.N
        self.Par = [-1] * self.N
        self.stack = [self.start]
        self.used[self.start] = True
        while self.stack:
            v = self.stack.pop()
            if v == self.finish:
                d = self.Flow[v]
                while v != self.start:
                    nv = self.Par[v]
                    self.graph[nv][v] -= d
                    self.graph[v][nv] += d
                    v = nv
                return d
            for i, (nv, ncap) in enumerate(self.graph[v].items()):
                if not self.used[nv] and ncap > 0:
                    self.used[nv] = True
                    self.stack.append(nv)
                    self.Par[nv] = v
                    self.Flow[nv] = min(self.Flow[v], ncap)
        return 0

    # solve
    def flow(self):
        flow = 0
        while True:
            f = self.dfs()
            if f == 0:
                return flow
            flow += f


input = sys.stdin.readline

INF = 10**18

H, W = map(int, input().split())
V = H + W


def make():
    state = [list(input().rstrip()) for _ in range(H)]
    graph = [{} for _ in range(V + 2)]

    start = V
    finish = V + 1

    for h in range(H):
        for w in range(W):
            u, v = h, w + H
            if state[h][w] == "o":
                graph[u][v] = 1
                graph[v][u] = 1
            if state[h][w] == "S":
                graph[v][start] = INF
                graph[start][v] = INF
                graph[u][start] = INF
                graph[start][u] = INF
            if state[h][w] == "T":
                graph[u][finish] = INF
                graph[finish][u] = INF
                graph[v][finish] = INF
                graph[finish][v] = INF

    return graph, start, finish


def main():
    graph, start, finish = make()
    ff = FordFulkerson(start, finish, graph)
    ans = ff.flow()

    if ans > INF // 2:
        print(-1)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
