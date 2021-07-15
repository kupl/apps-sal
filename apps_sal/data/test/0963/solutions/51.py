N, K = list(map(int, input().split()))
MOD = 998244353
L = [0] * K
R = [0] * K
for i in range(K):
    L[i], R[i] = list(map(int, input().split()))

dp = [0] * (N + 1)  # dpを到達方法の累積和のリストにする
dp[1] = 1

for i in range(1, N):
    for e in range(K):  # K=iの時の累積和の範囲
        left = max(0, i - R[e])  # 左側：とりうる一番小さいIdx
        right = max(0, i - L[e] + 1)  # 右側：とりうる一番大きいIdx
        dp[i + 1] += dp[right] - dp[left]  # i+1番目のdpはdpの右ー左
    dp[i + 1] += dp[i]  # 累積和（＝現在の数字＋一つ前の累積和）にするために一つ前のdpを足す
    dp[i + 1] %= MOD
print(((dp[N] - dp[N - 1]) % MOD))

