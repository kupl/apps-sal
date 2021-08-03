N = int(input())
dp = [i for i in range(N + 1)]

for i in range(1, 7):
    for j in range(9**i, N + 1):
        dp[j] = min(dp[j], dp[j - 9**i] + 1)
for i in range(1, 7):
    for j in range(6**i, N + 1):
        dp[j] = min(dp[j], dp[j - 6**i] + 1)
print(dp[N])
