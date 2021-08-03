N = int(input())
# 初期化
dp = [0] * N
for i in range(10):
    if 6**i - 1 < N:
        dp[6**i - 1] = 1
for i in range(10):
    if 9**i - 1 < N:
        dp[9**i - 1] = 1

# dp
for k in range(1, N):
    if dp[k] != 1:
        dp_list = []
        for j in range(10):
            if k >= 6**j:
                dp_list.append(dp[k - 6**j])
            if k >= 9**j:
                dp_list.append(dp[k - 9**j])

        dp[k] = 1 + min(dp_list)

print(dp[N - 1] % 1000000007)
