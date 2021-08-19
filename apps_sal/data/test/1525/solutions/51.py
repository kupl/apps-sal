H, W, K = map(int, input().split())
MOD = 10**9 + 7


def check(bit):
    pre_b = '0'
    for b in bit:
        if b == '1' and pre_b == '1':
            return False
        pre_b = b
    return True


# dp[h][w]:上からh段目での操作を終了した時点でw番目のあみだにいる場合の数
dp = [[0] * (W + 2) for h in range(H + 1)]
dp[0][1] = 1

# ある段における横線の配置を全探索してw-1 <-> wに横線がある数
lines = [0] * (W + 1)
c = 0
for i in range(2**(W - 1)):
    if not check(bin(i)[2:]):
        continue
    c += 1
    for w in range(W - 1):
        lines[w + 1] += (i & 1 << w) > 0


# 配るDP
for h in range(H):
    for w in range(1, W + 1):
        x, z = lines[w - 1], lines[w]
        y = c - x - z
        dp[h + 1][w - 1] = (dp[h + 1][w - 1] + dp[h][w] * x % MOD) % MOD
        dp[h + 1][w] = (dp[h + 1][w] + dp[h][w] * y % MOD) % MOD
        dp[h + 1][w + 1] = (dp[h + 1][w + 1] + dp[h][w] * z % MOD) % MOD

print(dp[-1][K])
