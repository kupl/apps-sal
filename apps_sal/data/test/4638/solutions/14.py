from math import *
(n, k) = map(int, input().split())
dp = [[float('inf'), float('inf')] for i in range(2 * 10 ** 5 + 5)]
dp[0] = [0, k]
esc = list(map(int, input().split()))
asc = list(map(int, input().split()))
print(0, end=' ')
for i in range(1, n):
    dp[i][0] = min(dp[i - 1]) + esc[i - 1]
    dp[i][1] = min(dp[i - 1][1], dp[i - 1][0] + k) + asc[i - 1]
    print(min(dp[i]), end=' ')
