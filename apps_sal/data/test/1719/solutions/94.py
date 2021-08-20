import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
MOD = 10 ** 9 + 7
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(101)]
dp[0][3][3][3] = 1
for length in range(n):
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                if dp[length][c1][c2][c3] == 0:
                    continue
                for a in range(4):
                    if a == 2 and c1 == 1 and (c2 == 0):
                        continue
                    if a == 2 and c1 == 0 and (c2 == 1):
                        continue
                    if a == 1 and c1 == 2 and (c2 == 0):
                        continue
                    if a == 2 and c1 == 1 and (c3 == 0):
                        continue
                    if a == 2 and c2 == 1 and (c3 == 0):
                        continue
                    dp[length + 1][a][c1][c2] += dp[length][c1][c2][c3]
                    dp[length + 1][a][c1][c2] %= MOD
ans = 0
for c1 in range(4):
    for c2 in range(4):
        for c3 in range(4):
            ans += dp[n][c1][c2][c3]
            ans %= MOD
print(ans)
