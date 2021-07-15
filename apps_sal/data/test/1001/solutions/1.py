n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
dp[n] = 0
cur = s[n]
for i in range(n - 1, 0, -1):
    dp[i] = cur
    cur = max(cur, s[i] - dp[i])
print(dp[1])

