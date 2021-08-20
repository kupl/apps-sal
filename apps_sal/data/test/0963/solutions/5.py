(n, k) = map(int, input().split())
q = [tuple(map(int, input().split())) for _ in range(k)]
dp = [0] * (n + 5)
MOD = 998244353
cnt = 1
for i in range(1, n + 5):
    cnt += dp[i]
    cnt %= MOD
    for p in q:
        if i + p[0] < n + 5:
            dp[i + p[0]] += cnt
            dp[i + p[0]] %= MOD
        if i + p[1] + 1 < n + 5:
            dp[i + p[1] + 1] -= cnt
            dp[i + p[1] + 1] %= MOD
print(dp[n])
