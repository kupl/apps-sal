N, K = map(int, input().split())
import numpy as np
#対称性を利用して点を単位格子K*2Kに圧縮
_2K, _4K = 2*K, 4*K
shape = (_2K+1,_4K+1) #後でK*2Kに圧縮
Grd = np.zeros(shape,dtype='int64')
for _ in range(N):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == 'B':
        x, y = x%_2K, y%_2K
    else: 
        x, y = (x+K)%_2K, y%_2K
    #点について、2K*2K -> K*2Kの調整。次は等価、(K+i,K+j)==(i,j),(i,K+j)==(i+K,j)
    if x >= K and y >= K: x -= K; y -= K
    if x < K and y >= K: x += K; y -= K
    #この点がK*Kの黒色正方形内に入る。正方形を特徴づけるには左下の座標だけで十分。
    #⇒１つの点はK**2個の塗り方に+1の影響を与える。
    #毎回2K**2のマスにアクセスするとTLEするため、あとで累積和(計算量O(K**2))を取った時に+1される範囲が等しくなるように調整する(隣接差分を取る)。
    #K=3の場合
    #[[1 1 1 0 0 0]    [[ 1 0 0 -1 0 0  0]
    # [1 1 1 0 0 0]     [ 0 0 0  0 0 0  0]
    # [1 1 1 0 0 0]  => [ 0 0 0  0 0 0  0]
    # [0 0 0 0 0 0]     [-1 0 0  1 0 0  0]
    # [0 0 0 0 0 0]     [ 0 0 0  0 0 0  0]
    # [0 0 0 0 0 0]]    [ 0 0 0  0 0 0  0]
    #                   [ 0 0 0  0 0 0  0]
    
    Grd[y, x] += 1
    Grd[y+K, x+K] += 1
    Grd[y+K, x] += -1
    Grd[y, x+K] += -1
del x, y, c

#2重累積和計算
Grd = Grd.cumsum(axis=1).cumsum(axis=0)
#2K*4K -> K*2Kへ圧縮
Grd = Grd[:,:_2K] +Grd[:,_2K:_4K]
Grd = Grd[:K,:] +np.concatenate((Grd[K:_2K,K:_2K],Grd[K:_2K,:K]),axis=1) 

ans = Grd.max()
print(ans)
