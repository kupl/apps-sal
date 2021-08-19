import sys
from collections import deque
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


class EDOMONDS_KARP:

    def __init__(self, N, s, t):
        self.N = N
        self.s = s
        self.t = t
        self.cap = [[0] * N for _ in range(N)]
        self.link = [[] for _ in range(N)]

    def add_edge(self, u, v, c):
        self.cap[u][v] = c
        self.link[u].append(v)
        self.link[v].append(u)

    def max_flow(self):
        N = self.N
        s = self.s
        t = self.t
        f = 0
        flow = [[0] * N for _ in range(N)]
        while True:
            (m, prev) = self.bfs(flow)
            if m == 0:
                break
            f += m
            v = t
            while v != s:
                u = prev[v]
                flow[u][v] += m
                flow[v][u] -= m
                v = u
        return (f, flow)

    def bfs(self, flow):
        N = self.N
        s = self.s
        t = self.t
        cap = self.cap
        link = self.link
        prev = [-1] * N
        prev[s] = -2
        m = [0] * N
        m[s] = float('inf')
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


def main():
    INF = float('inf')
    N = int(readline())
    A = list(map(int, readline().split()))
    (S, T) = (0, N + 1)
    EK = EDOMONDS_KARP(N + 2, S, T)
    add = EK.add_edge
    for i in range(1, N + 1):
        a = A[i - 1]
        if a <= 0:
            add(S, i, -a)
        else:
            add(i, T, a)
        for j in range(2, N // i + 1):
            add(i, i * j, INF)
    (f, _) = EK.max_flow()
    print(sum([x for x in A if x > 0]) - f)


def __starting_point():
    main()


__starting_point()
