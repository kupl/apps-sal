(n, s, k) = map(int, input().split())
s -= 1
r = list(map(int, input().split()))
INF = float('inf')
c = input()
dp = [[] for i in range(n)]


def calc(u):
    if dp[u]:
        return
    dp[u] = [0] * (r[u] + 1) + [INF] * (k - r[u])
    for i in range(n):
        if c[u] != c[i] and r[i] > r[u]:
            calc(i)
            d = abs(u - i)
            for j in range(r[u] + 1, k + 1):
                dp[u][j] = min(dp[u][j], dp[i][j - r[u]] + d)


ans = INF
for i in range(n):
    calc(i)
    ans = min(ans, abs(i - s) + dp[i][k])
if ans == INF:
    print(-1)
else:
    print(ans)
