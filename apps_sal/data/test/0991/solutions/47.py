from heapq import heappush, heappop
import sys
(N, M, S) = map(int, input().split())
S = min(S, 2500)
INF = 10 ** 18
dp = [[INF] * 2501 for _ in range(N)]
way = [[] for _ in range(N)]
for _ in range(M):
    (u, v, a, b) = map(int, input().split())
    way[u - 1].append((v - 1, a, b))
    way[v - 1].append((u - 1, a, b))
CD = [tuple(map(int, input().split())) for _ in range(N)]
q = [(0, 0, S)]
while q:
    (t, u, s) = heappop(q)
    for (nxt, a, b) in way[u]:
        if s >= a:
            if dp[nxt][s - a] > t + b:
                dp[nxt][s - a] = t + b
                heappush(q, (t + b, nxt, s - a))
    (c, d) = CD[u]
    nc = min(2500, c + s)
    nt = t + d
    if nt < dp[u][nc]:
        dp[u][nc] = nt
        heappush(q, (nt, u, nc))
for i in range(1, N):
    print(min(dp[i]))
