import numpy as np
N = int(input())
dp = np.zeros((N + 1, 5, 5, 5), dtype=np.int64)
# dp[文字列の長さ][3文字前][2文字前][1文字前]
# 0:dummy A:1, C:2, G:3, T:4
p = 10**9 + 7
dp[0, 0, 0, 0] = 1
for n in range(N):
    for i in range(5):  # 3文字前
        for j in range(5):
            for k in range(5):
                for l in range(1, 5):  # 今回追加する文字#0 : dummmyは初期条件の為なので回さない
                    if j == 1 and k == 3 and l == 2:
                        continue  # AGC
                    if j == 3 and k == 1 and l == 2:
                        continue  # GAC
                    if j == 1 and k == 2 and l == 3:
                        continue  # ACG
                    if i == 1 and k == 3 and l == 2:
                        continue  # A?GC
                    if i == 1 and j == 3 and l == 2:
                        continue  # AG?C
                    dp[n + 1, j, k, l] += dp[n, i, j, k]
                    dp[n + 1, j, k, l] %= p
ans = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            ans += dp[N, i, j, k]
            ans %= p
print(ans)
