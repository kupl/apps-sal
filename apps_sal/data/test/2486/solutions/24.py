import numpy as np
import itertools

N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()


def check(i):  # i番目のカードを使わなかった時
    dp = np.zeros(K, dtype=np.bool)  # 配列の初期化
    # 本来dp[x][y]の配列を用意すべきだけど、一回見たらそれ以降は見ないから上書きしていく
    # xが何であろうか、作れるかどうかだけが大切
    #dp: kが作れるかどうかだけを記録している
    dp[0] = True
    # print (dp)
    for j in itertools.chain(a[:i], a[i + 1:]):  # i番目を除いたリストを走査
        dp[j:] = np.logical_or(dp[j:], dp[:-j])  # ある数jを使うと、j以降のもの(N-j)個と前から(N-j)個のどちらかがTrueのものは作れる
    return not dp[-a[i]:].any()  # dpのK-a[i]からKの範囲どれかにTrueがあるとFalseを返す

# 詳しくはノート参照


# aを昇順並べた後の走査で、
# a_iが必要な時、a_(i+1)も必要
# -->二分探索によりlog Nで探索

la = -1
ua = N
while ua - la > 1:
    mid = (ua + la) // 2
    if check(mid):
        la = mid
    else:
        ua = mid

print(ua)
