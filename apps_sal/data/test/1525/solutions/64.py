import sys
readline = sys.stdin.readline

# 0-indexedで考える
# 縦棒はW本、横棒を置ける場所は一行あたりW - 1箇所となる
# ・iとi + 1の間に横棒を引いた場合の数
# ・iから移動せずにそのままになる場合の数
# をそれぞれ求める

# LINE[i] = iとi + 1の間に横棒を引いた場合の数。
# POINT[i] = iから横棒が出ていない場合の数
# それぞれDPで求める

H, W, K = list(map(int, readline().split()))
DIV = 1000000007

# dp[i][j] = 間隔iまで処理したときに、j番目の間隔に棒がある(0,1)場合の数
LINE = [-1] * (W - 1)
for i in range(W - 1):
    # iとi + 1の間に棒がある場合
    dp = [[0] * 2 for j in range(W - 1)]
    if i == 0:
        dp[0][0] = 0
        dp[0][1] = 1
    else:
        dp[0][0] = 1
        dp[0][1] = 1
    for j in range(1, W - 1):
        if j == i:
            dp[j][0] = 0
            dp[j][1] = dp[j - 1][0]
        else:
            dp[j][0] += dp[j - 1][0] + dp[j - 1][1]
            dp[j][1] += dp[j - 1][0]
    LINE[i] = dp[-1][0] + dp[-1][1]
    LINE[i] %= DIV

POINT = [-1] * W
# 点iからまっすぐ下がる場合の数
# iから右に棒を引く/引かない場合の数を数える
for i in range(W):
    # i - 1にもiにも棒がない場合
    dp = [[0] * 2 for j in range(W)]
    if i - 1 == 0 or i == 0:
        dp[0][0] = 1
        dp[0][1] = 0
    else:
        dp[0][0] = 1
        dp[0][1] = 1
    for j in range(1, W):
        if j == i - 1 or j == i:
            dp[j][1] = 0
            dp[j][0] += dp[j - 1][0] + dp[j - 1][1]
        else:
            dp[j][0] += dp[j - 1][0] + dp[j - 1][1]
            if j == W - 1:
                dp[j][1] = 0
            else:
                dp[j][1] += dp[j - 1][0]
    POINT[i] = dp[-1][0] + dp[-1][1]
    POINT[i] %= DIV

# ここからDP
# dp[i][j] = あみだのi段目でjにいる場合の数

dp = [[0] * W for i in range(H + 1)]
dp[0][0] = 1

for i in range(1, len(dp)):
    for j in range(W):
        # jを出発点にして遷移する
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1] * LINE[j - 1]
        dp[i][j] += dp[i - 1][j] * POINT[j]
        if j + 1 < W:
            dp[i][j] += dp[i - 1][j + 1] * LINE[j]

        dp[i][j] %= DIV

print((dp[H][K - 1]))
