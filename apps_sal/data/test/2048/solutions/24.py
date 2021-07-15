from math import inf

n = int(input())

s = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))

dp = [[0, inf, inf, inf][:] for i in range(n)]
dp[0][1] = c[0]

for j in range(1, 4):
    for i in range(1, n):
        for k in reversed(list(range(i))):
            if j == 1 or s[k] < s[i]:
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + c[i])

r = min(x[3] for x in dp)
if r == inf:
    print(-1)
else:
    print(r)


