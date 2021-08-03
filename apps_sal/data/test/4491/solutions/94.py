n = int(input())
dp = [[0 for i in range(n)] for i in range(2)]
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

dp[0][0] = a1[0]
for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + a1[i]
dp[1][0] = dp[0][0] + a2[0]

for i in range(1, n):
    dp[1][i] = max(dp[0][i] + a2[i], dp[1][i - 1] + a2[i])

print((dp[1][-1]))
