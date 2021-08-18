Limit = 2000
CMB = [[0] * (Limit + 1) for _ in range(Limit + 1)]


def cmb_table(Limit):
    for i in range(Limit + 1):
        for j in range(Limit + 1):
            if j == 0 or j == i:
                CMB[i][j] = 1
            else:
                CMB[i][j] = CMB[i - 1][j - 1] + CMB[i - 1][j]


cmb_table(Limit)
N, K = list(map(int, input().split()))
MOD = pow(10, 9) + 7
red = N - K
blue = K
for i in range(1, K + 1):
    p = CMB[blue - 1][i - 1] % MOD
    if i - 1 > red:
        print((0))
    else:
        ans = p * CMB[red + 1][i] % MOD
        print(ans)
