n = int(input())

c = input().split(" ")

for i in range(n):
    c[i] = int(c[i])

norm = ["" for i in range(n)]
rev = ["" for i in range(n)]

for i in range(n):
    norm[i] = input()
    rev[i] = norm[i][::-1]

MAX = 1e18

dp = [[MAX for i in range(2)] for i in range(n)]
dp[0][0] = 0
dp[0][1] = c[0]

for i in range(1, n):
    if norm[i] >= rev[i-1]:
        dp[i][0] = min(dp[i][0], dp[i-1][1])
    if norm[i] >= norm[i-1]:
        dp[i][0] = min(dp[i][0], dp[i-1][0])
    if rev[i] >= rev[i-1]:
        dp[i][1] = min(dp[i][1], dp[i-1][1]+c[i])
    if rev[i] >= norm[i-1]:
        dp[i][1] = min(dp[i][1], dp[i-1][0]+c[i])

ans = min(dp[n-1][0], dp[n-1][1])
if ans == MAX:
    print(-1)
else:
    print(ans)
