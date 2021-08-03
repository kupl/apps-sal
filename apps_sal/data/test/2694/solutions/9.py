# dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
def ipnl(n): return [int(input()) for _ in range(n)]


def inp(): return int(input())
def ip(): return [int(w) for w in input().split()]


n, m, k = ip()
laz = [ip() for i in range(k)]
dp = [[1 for i in range(m + 1)] for j in range(n + 1)]
for j in laz:
    x, y, t, f = j
    dp[x][y] = 0
    for i in range(1, n + 1):
        reach = i + x - t - abs(y - i)
        if reach > 0 and reach % f == 0:
            dp[i][y] = 0
    for i in range(1, m + 1):
        reach = i + y - t - abs(x - i)
        if reach > 0 and reach % f == 0:
            dp[x][i] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cur, left, up = dp[i][j], dp[i][j - 1], dp[i - 1][j]
        dp[i][j] = cur * left or cur * up

if dp[-1][-1]:
    print("YES")
    print(n + m - 2)
else:
    print("NO")
