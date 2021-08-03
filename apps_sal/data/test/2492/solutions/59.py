import numpy as np
n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))
a.sort()
p = a[a > 0]
z = np.count_nonzero(a == 0)
m = a[a < 0]
r = 10**19
l = -r
while r - l > 1:
    # 区間[l,r]を半分に分けて探索。最終的にrが求める値になるようにする。
    # b以下のものがk個以上あるような、最小のbを求める。bを大きくする→b以下のものも増える。b以下のものがめちゃくちゃある→bを減らす。
    b = (l + r) // 2
    c = 0
    if b >= 0:
        c += z * n
    # 配列aに対し、配列b//pの要素たちをそれぞれsearchsortedする。結果の配列はb//pと同じ形になる。
    c += a.searchsorted(b // p, side='right').sum()
    # 配列aに対し、配列b//mの要素たちをそれぞれsearchsortedする。結果の配列はb//mと同じ形になる。
    c += n * len(m) - a.searchsorted(-(-b // m), side='left').sum()
    c -= np.count_nonzero(a * a <= b)
    if c // 2 >= k:
        r = b
    else:
        l = b
print(r)
