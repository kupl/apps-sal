import math
def R(): return map(int, input().split())


ax, ay, bx, by, tx, ty = R()
n = int(input())
dp = [[0] * (n + 1) for i in range(4)]
for i in range(n):
    x, y = R()
    da, db, dt = ((x - ax) ** 2 + (y - ay) ** 2) ** 0.5, ((x - bx) ** 2 + (y - by) ** 2) ** 0.5, ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5
    dp[0][i] = dp[0][i - 1] + dt * 2
    dp[1][i] = min(dp[0][i - 1] + db + dt, dp[1][i - 1] + dt * 2 if i else math.inf)
    dp[2][i] = min(dp[0][i - 1] + da + dt, dp[2][i - 1] + dt * 2 if i else math.inf)
    dp[3][i] = min(dp[1][i - 1] + da + dt, dp[2][i - 1] + db + dt, dp[3][i - 1] + dt * 2) if i else math.inf
print(min(dp[3][n - 1], dp[2][n - 1], dp[1][n - 1]))
