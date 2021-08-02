n, k = list(map(int, input().split()))
s = []
for _ in range(k):
    l, r = list(map(int, input().split()))
    s.append((l, r + 1))

dp = [0] * (n + 1)    # dp[i+1]: Num of ways to reach cell i (0-based).
dif = [0] * (n + 1)   # dif[i] = dp[i] - dp[i-1] for  i > 0.

dif[1] = 1
dif[2] = -1
for i in range(1, n + 1):
    dp[i] = (dp[i - 1] + dif[i]) % 998244353
    for l, r in s:
        if i + l <= n:
            dif[i + l] += dp[i]
        if i + r <= n:
            dif[i + r] -= dp[i]

print(dp[-1])
