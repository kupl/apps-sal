N = int(input())
dp = [N] * 110000
dp[0] = 0

for i in range(N):
    j = 0
    while i + 9 ** j <= N:
        dp[i + 9 ** j] = min(dp[i + 9 ** j], dp[i] + 1)
        j += 1
    k = 0
    while i + 6 ** k <= N:
        dp[i + 6 ** k] = min(dp[i + 6 ** k], dp[i] + 1)
        k += 1

print(dp[N])
