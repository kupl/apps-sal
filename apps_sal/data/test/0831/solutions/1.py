from heapq import heappush, heappop


class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr]) - 1])

    def flow(self, s, t, f):
        N = self.N
        G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0] * N
        prv_v = [0] * N
        prv_e = [0] * N

        while f:
            dist = [INF] * N
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                for i, (w, cap, cost, _) in enumerate(G[v]):
                    if cap > 0 and dist[w] > dist[v] + cost + H[v] - H[w]:
                        dist[w] = r = dist[v] + cost + H[v] - H[w]
                        prv_v[w] = v
                        prv_e[w] = i
                        heappush(que, (r, w))
            if dist[t] == INF:
                return -1

            for i in range(N):
                H[i] += dist[i]

            d = f
            v = t
            while v != s:
                d = min(d, G[prv_v[v]][prv_e[v]][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prv_v[v]
        return res


T = input()
need = [0] * 30
for t in T:
    need[ord(t) - ord('a')] += 1
have = [[0] * 30 for _ in range(110)]
N = int(input())
a = [0] * 110

for i in range(N):
    v = input().split()
    S = v[0]
    a[i] = int(v[1])
    for s in S:
        have[i][ord(s) - ord('a')] += 1

V = 30 + N + 10
flow = MinCostFlow(V)

start = 30 + N + 5
target = 30 + N + 6
for c in range(26):
    flow.add_edge(start, c, need[c], 0)
    for j in range(N):
        flow.add_edge(c, 30 + j, have[j][c], 0)

for i in range(N):
    flow.add_edge(30 + i, target, a[i], i + 1)

ans = flow.flow(start, target, len(T))
print(ans)
