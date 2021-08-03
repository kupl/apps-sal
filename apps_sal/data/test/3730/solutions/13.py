n = int(input())
a = list(map(int, input().split()))

INF = 10 ** 9

dp = [[-INF] * 3 for i in range(n)]
for i in range(n):
    dp[i][0] = dp[i][2] = 1
    if i > 0:
        dp[i][1] = 2


def upd(i, cr, nx):
    dp[i + 1][nx] = max(dp[i + 1][nx], dp[i][cr] + 1)


for i in range(n - 1):
    for j in range(3):
        cur = dp[i][j]

        if j == 0:
            if a[i + 1] > a[i]:
                upd(i, j, 0)
                upd(i, j, 2)
            else:
                upd(i, j, 2)
        elif j == 1:
            if a[i + 1] > a[i]:
                upd(i, j, 1)
        else:
            if i > 0 and a[i + 1] > a[i - 1] + 1:
                upd(i, j, 1)


ans = 0
for i in range(n):
    ans = max(ans, max(dp[i]))

print(ans)
