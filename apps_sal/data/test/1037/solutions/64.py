# coding: utf-8
# Your code here!
#import numpy as np
N = int(input())
A = list(map(int, input().split()))
table = []

for i, a in enumerate(A):
    table.append([a, i])
table.sort()
dp = [[0for i in range(N + 1)]for j in range(N + 1)]
for i in range(1, N + 1):
    baby, pos = table.pop()
    dp[i][0] = dp[i - 1][0] + baby * abs(pos - i + 1)
    dp[0][i] = dp[0][i - 1] + baby * abs(pos - (N - i))
    for x in range(1, i):
        y = i - x
        dp[x][y] = max(dp[x - 1][y] + baby * abs(pos - x + 1), dp[x][y - 1] + baby * abs(pos - (N - y)))
print(int(max(dp[k][N - k] for k in range(N + 1))))
