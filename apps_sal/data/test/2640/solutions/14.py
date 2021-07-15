"""
参考
blog名  ベスパリブ    #プログラミングを主とした日記・備忘録です
URL     https://takeg.hatenadiary.jp/entry/2019/09/10/234417
id:     takeg
"""
# 初期入力
H,W = (int(x) for x in input().split())
S = [list(input()) for i in range(H)]
import numpy as np
S_np = (np.array(S) ==".")*1 #文字を数字に変換 Trueの所のみ演算、Falseは０


#置いたマス(i,j)から4方向探す
L = np.zeros((H,W),dtype=int)
R = np.zeros((H,W),dtype=int)
U = np.zeros((H,W),dtype=int)
D = np.zeros((H,W),dtype=int)
for i in range(W):
    # if S_int[i,j] ==0:これはいらない？⇒*S_npで１or０をかけてるから不要
    if i == 0: 
        L[:,i]      = S_np[:,i]
        R[:,W-i-1]  = S_np[:,W-i-1]
    else:
        L[:,i]      = (L[:,i-1] +1) * S_np[:,i]
        R[:,W-i-1]  = (R[:,W-i] +1) * S_np[:,W-i-1]

for i in range(H):
    if i == 0: 
        D[i,:]      = S_np[i,:]
        U[H-i-1,:]  = S_np[H-i-1,:]
    else:
        D[i,:]      = (D[i-1,:] +1) * S_np[i,:]
        U[H-i-1,:]  = (U[H-i,:] +1) * S_np[H-i-1,:]

#各方向を位置ごとに足す(numpyなら足すだけで行列の和) 
light = L + R + D + U -3 #基準点を4方向＋１してるからー３
light_max = np.max(light)
print(light_max)
