# https://codeforces.com/contest/933/problem/A
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
# do magic here

n = int(input())
arr = list(map(int, input().split()))
dp = [[0 for x in range(n)] for y in range(4)]

if arr[0] == 1:
    dp[0][0] = 1
else:
    dp[1][0] = 1

for i in range(1, n):
    if arr[i] == 1:
        dp[0][i] = dp[0][i - 1] + 1
    else:
        dp[0][i] = dp[0][i - 1]

for i in range(1, n):
    if arr[i] == 2:
        dp[1][i] = max(dp[1][i - 1] + 1, dp[0][i - 1] + 1)
    else:
        dp[1][i] = dp[1][i - 1]

for i in range(1, n):
    if arr[i] == 1:
        dp[2][i] = max([dp[2][i - 1] + 1, dp[1][i - 1] + 1, dp[0][i - 1] + 1])
    else:
        dp[2][i] = dp[2][i - 1]

for i in range(1, n):
    if arr[i] == 2:
        dp[3][i] = max([dp[3][i - 1] + 1, dp[2][i - 1] + 1, dp[1][i - 1] + 1, dp[0][i - 1] + 1])
    else:
        dp[3][i] = dp[3][i - 1]
# print(dp)
ans = max([dp[2][n - 1], dp[1][n - 1], dp[0][n - 1], dp[3][n - 1]])
print(ans)
