import math

#-桁dpなる書き方に挑戦-#
# -dp[k][j][i] 先頭からi桁目まで決めたときに,
# - 0でない要素をj個使っていて、k=0 小さいことが確定していない , k=1 確定


def solve(sN):
    dp = [[[0] * 105 for _ in range(4)] for _ in range(2)]  # 余分に取っておく。あとでlen(N)の要素を取り出し
    # 初期条件
    dp[0][0][0] = 1  # なにも決めていな状態。空集合。一致
    for i in range(len(sN)):
        for j in range(4):
            for k in range(2):
                nd = int(sN[i])  # sNの今の桁をnd。これから決める桁数字をdとする
                for d in range(10):
                    ni = i + 1; nj = j; nk = k
                    if d != 0:  # dが0でないならnjを１つ足す
                        nj += 1
                    if nj > K:  # 使える0以外の数字の個数を超えていたらだめ
                        continue
                    if k == 0:  # これまでの桁が一致している。
                        if d > nd:  # 数字が超えるからだめ
                            continue
                        if d < nd:  # 小さいなら、以降小さくなることが確定
                            nk = 1
                    dp[nk][nj][ni] += dp[k][j][i]
    ans = dp[0][K][len(sN)] + dp[1][K][len(sN)]  # 小さいものが確定＆一致
    return ans


sN = input()
K = int(input())
lenN = len(sN)
ans = solve(sN)
print(ans)
