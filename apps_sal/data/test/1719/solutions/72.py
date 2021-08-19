N = int(input())
MOD = 10 ** 9 + 7
R = range(5)
dp = [[[[0, 0, 0, 0, 0] for i in R] for j in R] for k in range(N + 1)]
dp[0][0][0][0] = 1
for x in range(N):
    for d in R:
        for c in R:
            for b in R:
                for a in range(1, 5):
                    if c == 1 and b == 2 and (a == 3):
                        continue
                    if c == 2 and b == 1 and (a == 3):
                        continue
                    if c == 1 and b == 3 and (a == 2):
                        continue
                    if d == 1 and b == 2 and (a == 3):
                        continue
                    if d == 1 and c == 2 and (a == 3):
                        continue
                    dp[x + 1][c][b][a] += dp[x][d][c][b]
                    dp[x + 1][c][b][a] %= MOD
ans = 0
for c in range(1, 5):
    for b in range(1, 5):
        for a in range(1, 5):
            ans += dp[N][c][b][a]
            ans %= MOD
print(ans)
