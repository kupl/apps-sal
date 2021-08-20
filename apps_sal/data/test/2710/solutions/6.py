import math
import sys


class FordFulkerson:

    class Edge:

        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V):
        self.V = V
        self.size = [0 for i in range(V)]
        self.G = [[] for i in range(V)]

    def add_edge(self, _from, to, cap):
        self.G[_from].append(self.Edge(to, cap, self.size[to]))
        self.G[to].append(self.Edge(_from, 0, self.size[_from]))
        self.size[_from] += 1
        self.size[to] += 1

    def dfs(self, v, t, f):
        if v == t:
            return f
        self.used[v] = True
        for i in range(self.size[v]):
            edge = self.G[v][i]
            if self.used[edge.to] is False and edge.cap > 0:
                d = self.dfs(edge.to, t, f if f < edge.cap else edge.cap)
                if d > 0:
                    self.G[v][i].cap -= d
                    self.G[edge.to][edge.rev].cap += d
                    return d
        return 0

    def max_flow(self, s, t):
        result = 0
        while True:
            self.used = [False for _ in range(self.V)]
            f = self.dfs(s, t, math.inf)
            if f == 0:
                return result
            result += f


def solve(r, w):
    """
    :param r:
    :param w:
    :return:
    """
    (num_cities, num_roads) = list(map(int, input().split()))
    original = list(map(int, input().split()))
    result = list(map(int, input().split()))
    flow_ford = FordFulkerson(num_cities * 2 + 2)
    T = num_cities + 1
    for i in range(num_roads):
        (p, q) = list(map(int, input().split()))
        flow_ford.add_edge(p, T + q - 1, 10 ** 9)
        flow_ford.add_edge(q, T + p - 1, 10 ** 9)
    for i in range(num_cities):
        flow_ford.add_edge(i + 1, T + i, 10 ** 9)
        flow_ford.add_edge(0, 1 + i, original[i])
        flow_ford.add_edge(T + i, 2 * num_cities + 1, result[i])
    ans = [[0 for i in range(num_cities)] for j in range(num_cities)]
    flow_ford.max_flow(0, 2 * num_cities + 1)
    for i in range(1, num_cities + 1):
        for v in flow_ford.G[i]:
            if v.to != 0:
                ans[i - 1][v.to - T] = flow_ford.G[v.to][v.rev].cap
    if sum(original) != sum(result):
        print('NO')
        return
    if [sum([ans[i][j] for i in range(num_cities)]) for j in range(num_cities)] == result:
        print('YES')
        for a in ans:
            print(' '.join(map(str, a)))
    else:
        print('NO')


def __starting_point():
    solve(sys.stdin, sys.stdout)


__starting_point()
