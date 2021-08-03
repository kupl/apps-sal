from heapq import heappush, heappop


class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def flow(self, s, t, f):
        N = self.N
        G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0] * N
        prv_v = [0] * N
        prv_e = [None] * N

        d0 = [INF] * N
        dist = [INF] * N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v
                        prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return None

            for i in range(N):
                H[i] += dist[i]

            d = f
            v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = MinCostFlow(8)

d.add_edge(0, 1, a[0], 0)
d.add_edge(0, 2, a[1], 0)
d.add_edge(0, 3, a[2], 0)

d.add_edge(1, 4, n, 0)
d.add_edge(1, 5, n, 1)
d.add_edge(1, 6, n, 0)

d.add_edge(2, 4, n, 0)
d.add_edge(2, 5, n, 0)
d.add_edge(2, 6, n, 1)

d.add_edge(3, 4, n, 1)
d.add_edge(3, 5, n, 0)
d.add_edge(3, 6, n, 0)

d.add_edge(4, 7, b[0], 0)
d.add_edge(5, 7, b[1], 0)
d.add_edge(6, 7, b[2], 0)


M = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])

print(d.flow(0, 7, n), M)
