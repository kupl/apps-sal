(n, z, w) = list(map(int, input().split()))
a = list(map(int, input().split()))
INF = 10 ** 10
coef = [-1, 1]
initial = [w, z]
func = [max, min]
turn = [0, 1]
dp = [[None] * 2 for _ in range(n)]
for i in range(n - 1, -1, -1):
    for (c, ini, f, t) in zip(coef, initial, func, turn):
        dp[i][t] = c * INF
        opo_card = a[i - 1] if i else ini
        dp[i][t] = f(dp[i][t], abs(a[-1] - opo_card))
        opo_t = (t + 1) % 2
        for j in range(i + 1, n):
            dp[i][t] = f(dp[i][t], dp[j][opo_t])
ans = dp[0][0]
print(ans)
