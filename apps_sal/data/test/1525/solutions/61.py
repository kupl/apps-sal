H, W, K = list(map(int, input().split()))

# 連続するn区間に橋をかける方法は何通りあるか
# kakekata[b][i] : bが0の時はi区間目に橋をかけない方法 bが1の時はi区間目に橋をかける方法 が何通りあるか
kakekata = [[0] * 10] + [[0] * 10]
kakekata[0][0] = 1
for i in range(8):
    kakekata[0][i + 1] = kakekata[0][i] + kakekata[1][i]
    kakekata[1][i + 1] = kakekata[0][i]


MOD = 10 ** 9 + 7
class modint:
    def __init__(self, x):
        self.x = x.x if isinstance(x, modint) else x % MOD
    def __str__(self): return str(self.x)
    __repr__ = __str__
    def __int__(self): return self.x
    __index__ = __int__
    def __add__(self, other): return modint(self.x + modint(other).x)
    def __sub__(self, other): return modint(self.x - modint(other).x)
    def __mul__(self, other): return modint(self.x * modint(other).x)
    def __pow__(self, other): return modint(pow(self.x, modint(other).x, MOD))
    def __floordiv__(self, other): return modint(self.x * pow(modint(other).x, MOD - 2, MOD))
    def __eq__(self, other): return self.x == modint(other).x
    def __ne__(self, other): return self.x != modint(other).x
    def __inv__(self): return pow(self.x, MOD - 2, MOD)


dp = [[modint(0)] * (W + 2) for h in range(H + 1)]
dp[0][1] += 1
for h in range(H):
    for w in range(1, W + 1):
        # 左に何区間あるか 右に何区間あるか
        l, r = w - 1, W - w

        # そのまま渡す
        dp[h + 1][w] += dp[h][w] * kakekata[0][l] * kakekata[0][r]
        # 右に渡す
        dp[h + 1][w + 1] += dp[h][w] * kakekata[0][l] * kakekata[1][r]
        # 左に渡す
        dp[h + 1][w - 1] += dp[h][w] * kakekata[1][l] * kakekata[0][r]

print((dp[H][K]))

