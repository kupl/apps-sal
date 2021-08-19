import sys
input = sys.stdin.readline
(n, q, c) = list(map(int, input().split()))
dp = []
for i in range(101):
    k = []
    for j in range(101):
        k.append([0] * 11)
    dp.append(k)
for i in range(n):
    (x, y, s) = list(map(int, input().split()))
    dp[x][y][s] += 1
for i in range(1, 101):
    for s in range(11):
        dp[i][0][s] += dp[i - 1][0][s]
for i in range(1, 101):
    for s in range(11):
        dp[0][i][s] += dp[0][i - 1][s]
for j in range(101):
    for i in range(101):
        if i > 0 and j > 0:
            for s in range(11):
                dp[i][j][s] += dp[i - 1][j][s] + dp[i][j - 1][s] - dp[i - 1][j - 1][s]
for j in range(q):
    (p, x1, y1, x2, y2) = list(map(int, input().split()))
    k = [0] * 11
    ans = 0
    for i in range(11):
        if x1 > 0 and y1 > 0:
            k[i] = dp[x2][y2][i] - dp[x2][y1 - 1][i] - (dp[x1 - 1][y2][i] - dp[x1 - 1][y1 - 1][i])
        elif x1 > 0 and y1 == 0:
            k[i] = dp[x2][y2][i] - dp[x1 - 1][y2][i]
        elif y1 > 0 and x1 == 0:
            k[i] = dp[x2][y2][i] - dp[x2][y1 - 1][i]
        else:
            k[i] = dp[x2][y2][i]
        if i >= c:
            if p == 0:
                r = i
            else:
                r = (p - 1) % (c + 1)
        elif p > c - i:
            r = (p - 1 - (c - i)) % (c + 1)
        else:
            r = p + i
        ans += k[i] * r
    print(ans)
