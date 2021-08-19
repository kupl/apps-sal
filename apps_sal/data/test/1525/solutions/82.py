# |-| | | | |
# のように一番左の一本が決まったとき、残りの
#     | | | |
# には、線を引く場所が3つある
# 線を引く場所がN個あるときの線の引き方の組み合わせは
# A[1] = 2, A[2] = 3, A[N] = A[N - 2] + A[N - 1]
# のほぼフィボナッチ数列
# 2,3,5,8,13...
# これをあらかじめ最大数ぶん求めておく
# 横棒W本に対して、W - 1個の間隔があり、そのうち端の2か所が埋まった状態が最大なのでW - 3
# これを求める

import sys
readline = sys.stdin.readline

DIV = 10 ** 9 + 7
H, W, K = map(int, readline().split())

P = [0] * max(W - 2 + 1, 3)
P[1], P[2] = 2, 3
for i in range(3, len(P)):
    P[i] = P[i - 1] + P[i - 2]

# [0, 2, 3, 5, 8, 13, 21, 34, ...]

# 通らない線は上記で算出できるので、通る線を考える
# 上からi段目まで終えた時点で、縦棒jにいるときの場合の数でDPする

dp = [[0 for j in range(W)] for i in range(H + 1)]

dp[0][0] = 1  # 上から0段目を終えた時点(まだ何もしていない)ときに0にいるので1通り


def calc(L, R):  # LとRの間に線を引いた場合の、残りの線の引き方
    #  print("calc L",L,"R",R)
    res = 1
    if 1 < L:
        # | | |-| Lが2のときはじめてスペースが1 (L - 1)できる
        res *= P[L - 1]
#    print("P[L - 2]",P[L - 2],"res",res)
        res %= DIV
    if (W - 1) - (R + 1) >= 1:
        # |-| | | R + 2 = W - 1のときはじめてスペースが1(W - R)できる
        #    print(min((W - 1) - (R + 1),len(P)))
        res *= P[(W - 1) - (R + 1)]
#    print("P[(W - 1) - (R + 1)]",min((W - 1) - (R + 1),len(P)),"res",res)
        res %= DIV
#  print(res,"通り")
    return res


# 右に移動する、左に移動する、何もしない、の3通りでDP
for i in range(H):
    for j in range(W):
        # 右に移動する
        if j + 1 < W:
            #      print("i",i,"j",j,"からi + 1",i + 1,"j + 1",j + 1,"に移動する dp[i][j]",dp[i][j],"dp[i + 1][j + 1]",dp[i + 1][j + 1])
            dp[i + 1][j + 1] += dp[i][j] * calc(j, j + 1)
            dp[i + 1][j + 1] %= DIV
#      print("i",i,"j",j,"からi + 1",i + 1,"j + 1",j + 1,"に移動した dp[i][j]",dp[i][j],"dp[i + 1][j + 1]",dp[i + 1][j + 1])
        # 左に移動する
        if j - 1 >= 0:
            #      print("i",i,"j",j,"からi + 1",i + 1,"j - 1",j - 1,"に移動する dp[i][j]",dp[i][j],"dp[i + 1][j - 1]",dp[i + 1][j - 1])
            dp[i + 1][j - 1] += dp[i][j] * calc(j - 1, j)
            dp[i + 1][j - 1] %= DIV
#      print("i",i,"j",j,"からi + 1",i + 1,"j - 1",j - 1,"に移動した dp[i][j]",dp[i][j],"dp[i + 1][j - 1]",dp[i + 1][j - 1])
        # 何もしない
#    print("i",i,"j",j,"からi",i,"j",j,"に移動する dp[i][j]",dp[i][j],"dp[i + 1][j]",dp[i + 1][j])
        dp[i + 1][j] += dp[i][j] * calc(j, j)  # 左端も右端も同じ
        dp[i + 1][j] % DIV
#    print("i",i,"j",j,"からi",i,"j",j,"に移動した dp[i][j]",dp[i][j],"dp[i + 1][j]",dp[i + 1][j])
#  for d in dp:
#    print(dp)


# i = H段目まで終えた時点で、j = K - 1にいる場合の数
print(dp[H][K - 1] % DIV)
