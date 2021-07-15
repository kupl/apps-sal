n, m, k = list(map(int, input().split()))
colors = list(map(int, input().split()))
costs = [list(map(int, input().split())) for _ in range(n)]

dp = [[[float('inf') for _ in range(k+1)] 
                     for _ in range(m+1)]
                     for _ in range(n+1)]

for i in range(m+1):
    for j in range(k+1):
        dp[0][i][j] = 0

for i in range(1, n+1):
    if colors[i-1] > 0:
        c = colors[i-1]
        for w in range(1, min(i, k)+1):
            dp[i][c][w] = min(dp[i][c][w], dp[i-1][c][w])
            for j in range(1, m+1):
                if j != c:
                    dp[i][c][w] = min(dp[i][c][w], dp[i-1][j][w-1])
    else:
        for w in range(1, min(i, k)+1):
            min1, min2 = float('inf'), float('inf')
            for j in range(1, m+1):
                if dp[i-1][j][w-1] < min1:
                    min2, min1 = min1, dp[i-1][j][w-1]
                else:
                    min2 = min(min2, dp[i-1][j][w-1]) 
            for j in range(1, m+1):
                dp[i][j][w] = min(dp[i][j][w], dp[i-1][j][w] + costs[i-1][j-1])
                if min1 != dp[i-1][j][w-1]:
                    dp[i][j][w] = min(dp[i][j][w], min1 + costs[i-1][j-1])
                else:
                    dp[i][j][w] = min(dp[i][j][w], min2 + costs[i-1][j-1])

res = float('inf')
for i in range(1, m+1):
    if dp[n][i][k] < res:
        res = dp[n][i][k]

print(-1 if res == float('inf') else res)

