N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges = [(i - 1, j - 1, c) for i, j, c in edges]

INF = int(10000)

dp = [[INF for _ in range(N)] for _ in range(N)]
for i, j, cost in edges:
    dp[i][j] = cost
    dp[j][i] = cost

for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[i][k] != INF and dp[k][j] != INF:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

count = 0
for i, j, cost in edges:
    if dp[i][j] < cost:
        count += 1

print(count)
