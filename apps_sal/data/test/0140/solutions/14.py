n, m, l = list(map(int, input().split(' '))) + [[]]
for i in range(n):
    l.append(list(map(int, input().split(' '))))
dp = [0] + [m for i in range(m)]
for i in range(1, m + 1):
    dp[i] = min(dp[i - 1] + 1, dp[i])
    for j in l:
        x = max(0, j[0] - j[1] - i)
        y = min(m, j[0] + j[1] + x)
        dp[y] = min(dp[y], dp[i - 1] + x)
print(dp[-1])
