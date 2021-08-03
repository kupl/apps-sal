N = int(input())

MOD = 10**9 + 7

dp = [[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]

dp[0][0][0][0] = 1
A = 1
C = 2
G = 3
T = 4

for i in range(N):
    for p in range(5):
        for q in range(5):
            for r in range(5):
                for s in range(1, 5):
                    if p == A and q == G and s == C:
                        continue
                    if p == A and r == G and s == C:
                        continue
                    if q == A and r == G and s == C:
                        continue
                    if q == G and r == A and s == C:
                        continue
                    if q == A and r == C and s == G:
                        continue
                    dp[i + 1][q][r][s] += dp[i][p][q][r]
                    dp[i + 1][q][r][s] %= MOD

ans = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            ans += dp[-1][i][j][k]
            ans %= MOD

print(ans)
