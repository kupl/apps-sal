(N, M) = list(map(int, input().split()))
INF = 10 ** 18
dp = [INF] * (1 << N)
dp[0] = 0
cost = [None] * M
target = [0] * M
for i in range(M):
    (cost[i], b) = list(map(int, input().split()))
    c = [int(x) for x in input().split()]
    for j in c:
        target[i] = target[i] | 1 << j - 1
for s in range(1 << N):
    for i in range(M):
        ns = s | target[i]
        dp[ns] = min(dp[ns], dp[s] + cost[i])
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
