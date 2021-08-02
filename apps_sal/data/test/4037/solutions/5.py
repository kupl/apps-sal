from sys import stdin
from sys import setrecursionlimit as SRL
SRL(10**7)
rd = stdin.readline
def rrd(): return list(map(int, rd().strip().split()))


n, r = rrd()


pos = []
neg = []

for i in range(n):
    a, b = rrd()
    if b < 0:
        neg.append([a, b])
    else:
        pos.append([a, b])

pos.sort(key=lambda x: x[0])
neg.sort(key=lambda x: x[0] + x[1])

ans = 0

for a, b in pos:

    if r >= a:
        r += b
        ans += 1
    else:
        break

dp = [[0] * 105 for _i in range(60005)]

for i in range(r + 10):
    for j in range(len(neg)):
        if i >= neg[j][0] and i + neg[j][1] >= 0:
            if j:
                dp[i][j] = max(dp[i][j], dp[i + neg[j][1]][j - 1] + 1, dp[i][j - 1])
            else:
                dp[i][j] = 1
        else:
            if j:
                dp[i][j] = dp[i][j - 1]


print(dp[r][len(neg) - 1] + ans)
