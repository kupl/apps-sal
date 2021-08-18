"""
累積和によるDP高速化
"""

N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]
mod = 998244353

S = []
for k in range(K):
    for i in range(LR[k][0], LR[k][1] + 1):
        S.append(i)

dp = [0] * N
sdp = [0] * (N + 1)

dp[0] = 1
sdp[1] = 1

for n in range(1, N):
    for lr in LR:
        left = max(0, n - lr[1])
        right = max(0, n - lr[0] + 1)
        dp[n] += sdp[right] - sdp[left]
        dp[n] %= mod
    sdp[n + 1] = (sdp[n] + dp[n]) % mod

res = dp[N - 1]
print(res)
