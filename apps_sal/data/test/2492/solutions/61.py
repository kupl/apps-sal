import numpy as np
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = np.array(a, dtype="int64")
a_minus = a[a < 0]
a_plus = a[a > 0]
a_zero = a[a == 0]
# print(a_plus)
l = - 10**19
r = 10**19


while r - l > 1:
    mid = (l + r) // 2
    # mid以下の個数を調べる
    cnt = 0
    # 正の数の組み合わせでmid以下の個数を調べる
    cnt += a.searchsorted(mid // a_plus, side="right").sum()
    # 負の数で同様
    cnt += (n - a.searchsorted((-mid - 1) // (-a_minus), side="right")).sum()
    # 同じ数の組み合わせ(差し引くよう)
    cnt -= np.count_nonzero(a * a <= mid)
    # ゼロも同様(mid>=0のときのみ)
    cnt += len(a_zero) * n if mid >= 0 else 0

    # 重複を割る
    cnt //= 2

    if cnt >= k:
        r = mid
    else:
        l = mid

print(r)
