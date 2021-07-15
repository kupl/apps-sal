n, k = list(map(int, input().split()))
sec = [tuple(map(int, input().split())) for _ in range(k)]

mod = 998244353
dp = [0] * n
sdp = [0] * (n+1)
dp[0] = 1
sdp[1] = 1
for i in range(1, n):
    for l, r in sec:
        dp[i] += sdp[max(i-l+1, 0)] - sdp[max(i-r, 0)]
        dp[i] %= mod
    sdp[i+1] = sdp[i] + dp[i]
    sdp[i+1] %= mod

print((dp[n-1]))

