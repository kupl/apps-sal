__author__ = 'epeshk'


def admod(a, b):
    a += b
    if a > 1000000000.0 + 7:
        a -= 1000000000.0 + 7
    return a


(n, k, d) = list(map(int, input().split()))
Dp = [[1, 0]]
for i in range(1, n + 1):
    Dp.append([0, 0])
    for j in range(1, k + 1):
        if i - j < 0:
            break
        if j < d:
            Dp[i][0] = admod(Dp[i][0], Dp[i - j][0])
            Dp[i][1] = admod(Dp[i][1], Dp[i - j][1])
        else:
            Dp[i][1] = admod(Dp[i][1], Dp[i - j][0])
            Dp[i][1] = admod(Dp[i][1], Dp[i - j][1])
print(int(Dp[n][1]))
