
N = input()
K = int(input())

dp = [[[0] * len(N) for _ in range(K + 1)] for _ in range(2)]
dp[0][0][0] = 0
dp[1][0][0] = 1
dp[0][1][0] = 1
dp[1][1][0] = max(0, int(N[0]) - 1)

man_k = 1
for i in range(1, len(N)):
    n = N[i]
    is_nonzero = 1 if n != '0' else 0
    man_k += is_nonzero
    if man_k <= K:
        dp[0][man_k][i] = dp[0][man_k - is_nonzero][i - 1]

    dp[1][0][i] = dp[1][0][i - 1]
    for k in range(1, K + 1):
        dp[1][k][i] = dp[1][k][i - 1] + dp[1][k - 1][i - 1] * 9
        if n != "0":
            dp[1][k][i] += dp[0][k - 1][i - 1] * (int(n) - 1) + dp[0][k][i - 1]

print(dp[0][K][-1] + dp[1][K][-1])
