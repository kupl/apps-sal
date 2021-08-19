n = int(input())
S = input()
A = [int(i) for i in input().split()]
INF = 10 ** 15
T = 'hard'
dp = [[INF] * (n + 1) for i in range(5)]
for i in range(5):
    dp[i][0] = 0
for (i, s) in enumerate(S):
    for (j, t) in enumerate('hard'):
        if s == t:
            dp[j][i + 1] = min(dp[j][i + 1], dp[j][i] + A[i])
            dp[j + 1][i + 1] = min(dp[j + 1][i + 1], dp[j][i])
        else:
            dp[j][i + 1] = min(dp[j][i + 1], dp[j][i])
print(min((dp[i][n] for i in range(4))))
