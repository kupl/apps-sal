from sys import stdin

n = int(stdin.readline())
h = [[], []]
h[0] = list(map(int, stdin.readline().split(' ')))
h[1] = list(map(int, stdin.readline().split(' ')))

dp = [[0 for i in range(n)], [0 for i in range(n)]]

dp[0][0] = h[0][0]
dp[1][0] = h[1][0]

for j in range(1, n):
   for i in [0, 1]:
      dp[i][j] = max(dp[i][j-1], h[i][j] + dp[i^1][j-1])

res = max(dp[0][n-1], dp[1][n-1])
print(res)

