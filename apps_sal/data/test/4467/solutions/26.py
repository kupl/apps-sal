import sys
input = sys.stdin.readline


class FordFulkerson:
    def __init__(self, n):
        self.N = n
        self.G = [[] for _ in range(n)]

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
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        f = INF = 10**9 + 7
        N = self.N
        while f:
            self.used = [0] * N
            f = self.dfs(s, t, INF)
            flow += f
        return flow


def main():
    n = int(input())
    red = [list(map(int, input().split())) for _ in range(n)]
    blue = [list(map(int, input().split())) for _ in range(n)]

    flow = FordFulkerson(n * 2 + 2)
    for i in range(n):
        flow.add_edge(0, i + 1, 1)
        flow.add_edge(n + i + 1, 2 * n + 1, 1)
        for j in range(n):
            if red[i][0] < blue[j][0] and red[i][1] < blue[j][1]:
                flow.add_edge(i + 1, n + j + 1, 1)

    ans = flow.flow(0, 2 * n + 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
