# -*- coding: utf-8 -*-
# 尺取り法

import numpy as np
n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))
a.sort()
posi = a[a > 0]
zero = a[a == 0]
nega = a[a < 0]
# print(posi)
# 2分探索, midより小さいものを数える
l = -10**18 - 1
r = 10**18 + 1
while r - l > 1:
    mid = (r + l) // 2
    cnt = 0
    if mid >= 0:
        cnt += len(zero) * n

    # a.searchsorted(v, side="left"): a[i-1] < v <= a[i]であるvのindexを返す
    # a.searchsorted(v, side="right"): a[i-1] <= v < a[i]であるvのindexを返す

    cnt += a.searchsorted(mid // posi, side="right").sum()
    cnt += (n - a.searchsorted(-(-mid // nega), side="left")).sum()
    cnt -= np.count_nonzero(a * a <= mid)
    cnt //= 2
    #print("mid:", mid)
    #print("mid//posi:", mid//posi)
    #print("search:", a.searchsorted(mid//posi,side="right"))
    #print("-(-mid//nega):", -(-mid//nega))
    #print("search:", a.searchsorted(-(-mid//nega),side="left"))
    #print("nonzero_count:", np.count_nonzero(a*a<=mid))
    #print("count:", cnt)
    #print('-' * 20)
    if cnt >= k:
        r = mid
    else:
        l = mid
print(r)
