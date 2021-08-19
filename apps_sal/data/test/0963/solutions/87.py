(N, K) = map(int, input().split())
L = [list(map(int, input().split())) for i in range(K)]
dp = [0 for i in range(N + 10)]
sdp = [0 for i in range(N + 11)]
dp[0] = 1
sdp[1] = 1
for i in range(1, N):
    for array in L:
        if i - array[-1] < 0:
            start = 0
        else:
            start = i - array[-1]
        if i - array[0] < 0:
            end = 0
        else:
            end = i - array[0] + 1
        dp[i] += sdp[end] - sdp[start]
    dp[i] = dp[i] % 998244353
    sdp[i + 1] = sdp[i] + dp[i]
print(dp[N - 1])
