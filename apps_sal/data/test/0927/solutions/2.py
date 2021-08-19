INF = float('inf')
cost = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
dp = [-INF] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    for a in A:
        if i - cost[a] >= 0:
            dp[i] = max(dp[i], dp[i - cost[a]] * 10 + a)
print(dp[N])
