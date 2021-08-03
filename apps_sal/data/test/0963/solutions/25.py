n, k = map(int, input().split())
mod = 998244353
S = []
for _ in range(min(n, k)):
    l, r = map(int, input().split())
    S.append((l, r + 1))
dp = [0] * (n + 1)
cum = [0] * (n + 1)
dp[1] = 1
cum[1] = 1
for i in range(2, n + 1):
    # もらうdp
    for l, r in S:
        ll = max(0, i - r)
        rr = max(0, i - l)
        dp[i] += cum[rr] - cum[ll]
        dp[i] %= mod
    cum[i] = (cum[i - 1] + dp[i]) % mod

print(dp[n])
