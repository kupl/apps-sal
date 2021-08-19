import math
N = int(input())
INF = 10 ** 10
dp = [0] * (N + 1)
for i in range(N + 1):
    dp[i] = INF
dp[0] = 0
W = [1, 6, 9]
for v in range(1, N + 1):
    for w in range(3):
        for x in range(int(math.log(N + 1, 6)) + 1):
            n = W[w] ** x
            if v - n < 0:
                continue
            dp[v] = min(dp[v], dp[v - n] + 1)
print(dp[N])
