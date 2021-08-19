(n, k) = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(k)]
mod = 998244353
dp = [0] * n
sdp = [0] * (n + 1)
dp[0] = 1
sdp[1] = 1
for i in range(1, n):
    tmp = 0
    for (l, r) in s:
        tmp += sdp[i - l + 1] - sdp[i - r]
    dp[i] = tmp % mod
    sdp[i + 1] = sdp[i] + dp[i]
print(dp[-1])
