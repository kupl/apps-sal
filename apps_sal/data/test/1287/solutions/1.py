import sys

n = int(input())
prob = [list(map(float, input().split())) for _ in range(n)]
dp = [[0.0]*(1 << n) for _ in range(n)]
dp[0][1] = 1.0

for mask in range(3, 1 << n):
    for i in range(n):
        if not (mask & (1 << i)):
            continue
        for j in range(n):
            if i != j and mask & (1 << j):
                dp[i][mask] = max(
                    dp[i][mask],
                    dp[i][mask - (1 << j)] * prob[i][j]
                    + dp[j][mask - (1 << i)] * prob[j][i]
                )

print(max(dp[i][-1] for i in range(n)))

