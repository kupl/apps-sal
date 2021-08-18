
import sys

infile = open("input.txt", "r")
outfile = open("output.txt", "w+")
sys.stdin = infile
sys.stdout = outfile
n = int(input())
t = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n + 1)]

for i in range(n):
    dp[i + 1] = dp[i][:]
    if (t[i] >= 0):
        dp[i + 1][0] += 1
    if (t[i] <= 0):
        dp[i + 1][1] += 1
ans = n
for i in range(0, n - 1):
    ans = min(ans, dp[i + 1][0] - dp[0][0] + dp[n][1] - dp[i + 1][1])
print(ans)
