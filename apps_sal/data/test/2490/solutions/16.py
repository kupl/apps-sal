S = input()
L = len(S)

INF = float('inf')
dp = [[INF] * (L + 1) for _ in range(2)]
dp[0][0] = 0

for i in range(L):
    d = int(S[-1 - i])
    dp[0][i + 1] = min(dp[0][i], dp[1][i]) + d
    dp[1][i + 1] = min(dp[0][i] + 10 - d + 1, dp[1][i] + 10 - d - 1)

print(min(dp[0][-1], dp[1][-1]))
