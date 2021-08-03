MOD = pow(10, 9) + 7
N = int(input())
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
dp[0][3][3][3] = 1  # 3333Sとくる場合は制約に何も引っかからない
#dp[i][j][k][l]: i文字目まで見て最後のの三文字がlkjであるような場合の数
# A=0, G=1, C=2, T=3

for i in range(N):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if dp[i][j][k][l] == 0:  # i文字目で条件にあてはまるものがないときは飛ばす。
                    continue
                for a in range(4):  # ダメな条件を飛ばす
                    if a == 2 and j == 1 and k == 0:  # AGC
                        continue
                    if a == 1 and j == 2 and k == 0:  # ACG
                        continue
                    if a == 2 and j == 0 and k == 1:  # GAC
                        continue
                    if a == 2 and j == 1 and l == 0:  # A?GC
                        continue
                    if a == 2 and k == 1 and l == 0:  # AG?c
                        continue
                    dp[i + 1][a][j][k] += dp[i][j][k][l] % MOD
ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[N][j][k][l]
ans = ans % MOD
print(ans)
