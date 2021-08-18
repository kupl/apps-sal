N, M = map(int, input().split())

issafe = [1] * (N + 1)
for i in range(M):
    a = int(input())
    issafe[a] = 0

dp = [0] * (N + 1)
dp[0] = 1
if issafe[1]:
    dp[1] = 1
for i in range(2, N + 1):
    if issafe[i - 1]:
        dp[i] += dp[i - 1]
    if issafe[i - 2]:
        dp[i] += dp[i - 2]
    dp[i] %= 10**9 + 7

print(dp[N])
