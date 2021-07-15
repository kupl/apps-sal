H, W, D = map(int, input().split())
Aindex = [0] * (H*W)
for h in range(H):
    w = 0
    for A in input().split():
        Aindex[int(A)-1] = (h,w)
        w += 1 

import numpy as np
v, h = int(np.ceil(H*W/D)), D
Mp = np.zeros((v, h), dtype='int64') #MpをMod D別に計算する予定
mp = lambda X, Y: abs(X[0]-Y[0]) + abs(X[1]-Y[1]) #魔力計算する関数
for x in range(D,H*W):
    i, j = divmod(x, D)
    Mp[i,j] = mp(Aindex[x], Aindex[x-D])
#縦軸方向に累積和を取っておき、後のクエリにO(1)で対応
Mp = Mp.cumsum(axis=0)

#クエリ処理
Q = int(input())
Query = [tuple(map(int, input().split())) for _ in range(Q)]
for l,r in Query:
    ans = Mp[divmod(r-1, D)] - Mp[divmod(l-1, D)]
    print(ans)
