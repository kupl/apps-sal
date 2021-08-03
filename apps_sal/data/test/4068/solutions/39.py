n, m = map(int, input().split())
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1

for _ in range(m):
    a = int(input())
    dp[a] = -1

for i in range(0, n - 1):
    if dp[i + 2] == -1:
        continue
    if dp[i] == -1 and dp[i + 1] == -1:
        dp[i + 2] = -1
    elif dp[i] == -1:
        dp[i + 2] = dp[i + 1]
    elif dp[i + 1] == -1:
        dp[i + 2] = dp[i]
    else:
        dp[i + 2] = dp[i] + dp[i + 1]

print(dp[n] % (10**9 + 7) if dp[n] != -1 else 0)
