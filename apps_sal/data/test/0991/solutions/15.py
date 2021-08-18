
from heapq import heappush, heappop


def resolve():
    INF = float('inf')
    maxMoney = 2502

    def Dijkstra(g):
        ans = {}
        dp = [[INF] * (maxMoney + 1) for _ in range(N)]
        hq = []
        heappush(hq, (0, 0, min(S, maxMoney)))
        while hq:
            t, v, s = heappop(hq)
            if t > dp[v][s]:
                continue
            if v not in ans:
                ans[v] = t
                if len(ans) == N:
                    break

            if s < maxMoney:
                c, d = CD[v]
                new_s = min(s + c, maxMoney)
                new_t = t + d
                if new_t < dp[v][new_s]:
                    dp[v][new_s] = new_t
                    heappush(hq, (new_t, v, new_s))

            for nv, cost, time in G[v]:
                if s < cost:
                    continue
                new_s = s - cost
                new_t = t + time
                if new_t < dp[nv][new_s]:
                    dp[nv][new_s] = new_t
                    heappush(hq, (new_t, nv, new_s))
        return ans

    N, M, S = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, coin, tm = list(map(int, input().split()))
        u, v = u - 1, v - 1
        G[u].append((v, coin, tm))
        G[v].append((u, coin, tm))
    CD = [list(map(int, input().split())) for _ in range(N)]

    ans = Dijkstra(G)
    for i in range(1, N):
        print((ans[i]))


def __starting_point():
    resolve()


__starting_point()
