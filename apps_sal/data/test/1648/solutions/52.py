Limit = 2000  # 上限を決める
CMB = [[0] * (Limit + 1) for _ in range(Limit + 1)]


def cmb_table(Limit):
    for i in range(Limit + 1):
        for j in range(Limit + 1):
            if j == 0 or j == i:  # 端っこの場合
                CMB[i][j] = 1
            else:
                CMB[i][j] = CMB[i - 1][j - 1] + CMB[i - 1][j]


cmb_table(Limit)  # これ必須！
# print(CMB[3][2])
N, K = list(map(int, input().split()))
MOD = pow(10, 9) + 7
red = N - K
blue = K
for i in range(1, K + 1):
    p = CMB[blue - 1][i - 1] % MOD
    # print(p,i)
    if i - 1 > red:
        print((0))
    else:
        ans = p * CMB[red + 1][i] % MOD
        print(ans)
