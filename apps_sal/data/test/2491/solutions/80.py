# ABC061 D - Score Attack
import sys
N, M = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(M)]

INF = 1 << 60
cost = [- INF] * (N + 1)
cost[1] = 0

for i in range(N):
    for n, nn, c in edge:
        if cost[nn] < cost[n] + c:
            # ベルマンフォード法の性質より、N回目に更新があるならinf
            if i == N - 1 and nn == N:
                print("inf")
                return
            cost[nn] = cost[n] + c

print(cost[N])
