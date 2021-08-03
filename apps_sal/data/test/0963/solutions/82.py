mod = 998244353
n, k = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(k)]
dp = [0] * (n + 1)
dp[1] = 1
dpsum = [0] * (n + 1)
dpsum[1] = 1

for i in range(2, n + 1):
    for s1, s2 in s:
        l = i - s2
        r = i - s1
        if r < 1:
            continue
        l = max(l, 1)
        dp[i] += (dpsum[r] - dpsum[l - 1]) % mod
    dpsum[i] = (dpsum[i - 1] + dp[i]) % mod
print(dp[-1] % mod)
