import sys
import bisect
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
INF = 10 ** 9
(anum, bnum, cnum) = [int(item) for item in input().split()]
k = anum + bnum + cnum
a = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]
c = [int(item) for item in input().split()]
holder = [0] * k
for item in a:
    holder[item - 1] = 0
for item in b:
    holder[item - 1] = 1
for item in c:
    holder[item - 1] = 2
dp = [[INF] * (k + 1) for _ in range(3)]
dp[0][0] = 0
dp[1][0] = 0
dp[2][0] = 0
for i in range(k):
    if holder[i] == 0:
        dp[0][i + 1] = min(dp[0][i + 1], dp[0][i])
        dp[1][i + 1] = min(dp[1][i + 1], dp[1][i] + 1)
        dp[2][i + 1] = min(dp[2][i + 1], dp[2][i] + 1)
        dp[1][i + 1] = min(dp[1][i + 1], dp[0][i] + 1)
        dp[2][i + 1] = min(dp[2][i + 1], dp[1][i] + 1)
        dp[2][i + 1] = min(dp[2][i + 1], dp[0][i] + 1)
    elif holder[i] == 1:
        dp[0][i + 1] = min(dp[0][i + 1], dp[0][i] + 1)
        dp[1][i + 1] = min(dp[1][i + 1], dp[1][i])
        dp[2][i + 1] = min(dp[2][i + 1], dp[2][i] + 1)
        dp[1][i + 1] = min(dp[1][i + 1], dp[0][i])
        dp[2][i + 1] = min(dp[2][i + 1], dp[1][i] + 1)
        dp[2][i + 1] = min(dp[2][i + 1], dp[0][i] + 1)
    elif holder[i] == 2:
        dp[0][i + 1] = min(dp[0][i + 1], dp[0][i] + 1)
        dp[1][i + 1] = min(dp[1][i + 1], dp[1][i] + 1)
        dp[2][i + 1] = min(dp[2][i + 1], dp[2][i])
        dp[1][i + 1] = min(dp[1][i + 1], dp[0][i] + 1)
        dp[2][i + 1] = min(dp[2][i + 1], dp[1][i])
        dp[2][i + 1] = min(dp[2][i + 1], dp[0][i])
ans = INF
for line in dp:
    ans = min(ans, line[-1])
print(ans)
