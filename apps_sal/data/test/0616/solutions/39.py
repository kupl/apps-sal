N, M = map(int, input().split())
INF = 10 ** 10
dp = [INF] * (2 ** N)
dp[0] = 0

for i in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    key = 0
    for j in range(len(c)):
        key += (1 << (c[j] - 1))
    for j in range(len(dp) - 1, -1, -1):
        if dp[j] == INF:
            continue
        dp[j | key] = min(dp[j | key], dp[j] + a)

print((dp[-1], -1)[dp[-1] == INF])
