import sys
from collections import deque
input = sys.stdin.readline


class Dinic:
    def __init__(self, v):
        self.vertice = v
        self.inf = int(1e9)
        self.graph = [[] for i in range(v)]
        self.level = [0] * v
        self.iter = [0] * v

    def add_edge(self, fr, to, cap):
        self.graph[fr].append([to, cap, len(self.graph[to])])
        self.graph[to].append([fr, 0, len(self.graph[fr]) - 1])

    def bfs(self, s):
        self.level = [-1] * self.vertice
        que = deque([])
        self.level[s] = 0
        que.append(s)

        while que:
            v = que.popleft()
            for i in range(len(self.graph[v])):
                e = self.graph[v][i]
                if e[1] > 0 and self.level[e[0]] < 0:
                    self.level[e[0]] = self.level[v] + 1
                    que.append(e[0])

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.graph[v])):
            self.iter[v] = i
            e = self.graph[v][i]
            if e[1] > 0 and self.level[v] < self.level[e[0]]:
                d = self.dfs(e[0], t, min(f, e[1]))
                if d > 0:
                    e[1] -= d
                    self.graph[e[0]][e[2]][1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow
            self.iter = [0] * self.vertice

            f = self.dfs(s, t, self.inf)
            while f:
                flow += f
                f = self.dfs(s, t, self.inf)


def main():
    n = int(input())
    red = [list(map(int, input().split())) for _ in range(n)]
    blue = [list(map(int, input().split())) for _ in range(n)]

    flow = Dinic(n * 2 + 2)
    for i in range(n):
        flow.add_edge(0, i + 1, 1)
        flow.add_edge(n + i + 1, 2 * n + 1, 1)
        for j in range(n):
            if red[i][0] < blue[j][0] and red[i][1] < blue[j][1]:
                flow.add_edge(i + 1, n + j + 1, 1)

    ans = flow.max_flow(0, 2 * n + 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
