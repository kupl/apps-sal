import numpy as np
import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))
pos = np.sort(a[a > 0])
neg = np.sort(np.abs(a[a < 0]))
zero = (a == 0).sum()

INF = 2 * (10**18)
l = -INF
r = INF
while(r - l > 1):
    mid = (l + r) // 2
    cnt = 0
    if mid >= 0:
        cnt = len(pos) * len(neg)  # (+) * (-)
        cnt += (len(pos) + len(neg)) * zero  # 0 * (non-zero)
        cnt += (zero * (zero - 1)) // 2  # 0 * 0
        x = np.searchsorted(pos, mid // pos, side='right').sum()  # (+) * (+)
        x += np.searchsorted(neg, mid // neg, side='right').sum()  # (-) * (-)
        x -= (pos * pos <= mid).sum()
        x -= (neg * neg <= mid).sum()
        cnt += x / 2
    else:
        # 積がmid以上になれば良い -> midよりも小さい
        cnt = (len(neg) - np.searchsorted(neg, abs(mid) // pos + (mid % pos != 0), side='left')).sum()
    #print(mid, cnt)
    # cnt := 積がmid以下になる物の数
    # k番目の数　-> それ以下のものがk個以上ある事が必要
    # cntがk個よりも少ない -> 条件を満たしていない
    # cntがそれ以上ならok
    if cnt < k:
        l = mid
    else:
        r = mid
print(r)
