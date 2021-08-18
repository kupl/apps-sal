n = int(input())
K = int(input())


def make_list(n):
    N = []
    while(n > 0):
        N.append(n % 10)
        n = n // 10
    N.reverse()
    return N


N = make_list(n)
m = len(N)
dp = [[[0 for k in range(K + 1)] for j in range(2)] for i in range(m)]
dp[0][0][0] = 1
dp[0][0][1] = N[0] - 1
dp[0][1][0] = 0
dp[0][1][1] = 1

for i in range(1, m):
    dp[i][0][0] = 1
    for k in range(1, K + 1):
        if N[i] == 0:
            dp[i][0][k] = dp[i - 1][0][k - 1] * 9 + dp[i - 1][0][k]
            dp[i][1][k] = dp[i - 1][1][k]
        else:
            dp[i][0][k] = dp[i - 1][0][k - 1] * 9 + dp[i - 1][0][k] + dp[i - 1][1][k] + dp[i - 1][1][k - 1] * (N[i] - 1)
            dp[i][1][k] = dp[i - 1][1][k - 1]
print((dp[m - 1][1][K] + dp[m - 1][0][K]))
