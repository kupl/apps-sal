import numpy as np
n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))
a.sort()

p = a[a > 0]
zeros = np.count_nonzero(a == 0)
m = a[a < 0]

# 数xが何番目に大きい積か計算。複数ある場合は最大値


def count(x):
    cnt = 0
    # 0以上だったらまず0の個数を足す
    if x >= 0:
        cnt += zeros * n  # 同じ要素の２じょうはあとで除くのでここでは気にせずかける
    # プラス部分のカウント
    # x//pはpをかけてもxを超えない数
    cnt += a.searchsorted(x // p, side='right').sum()
    # マイナス部分のカウント
    # マイナスは書けると大小が逆転する
    cnt += n * len(m) - a.searchsorted(-(-x // m), side='left').sum()
    # 二乗を引く
    cnt -= np.count_nonzero(a * a <= x)
    return cnt // 2


# 十分に大きい範囲
l, r = -10**19, 10**19
# r==lになるまで
while r - l > 1:
    mid = (r + l) // 2
    # 真ん中がk以上だったらrを小さくして再挑戦
    if count(mid) >= k:
        r = mid
    else:
        l = mid
print(r)
