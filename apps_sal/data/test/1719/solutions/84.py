n = int(input())
# {0:"A", 1:"C", 2:"G", 3:"T"}
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
dp[0][3][3][3] = 1
mod = 10 ** 9 + 7

for i in range(n):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    if m == 1 and l == 0 and k == 2: continue
                    if m == 2 and l == 1 and k == 0: continue
                    if m == 1 and l == 2 and k == 0: continue
                    if m == 1 and k == 2 and j == 0: continue
                    if m == 1 and l == 2 and j == 0: continue
                    
                    dp[i+1][k][l][m] += dp[i][j][k][l]
                    
ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[n][j][k][l]

print(ans % mod)
