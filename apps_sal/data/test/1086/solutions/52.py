import numpy as np
import itertools

H,W=map(int,input().split())
A=[list(map(int, input().split())) for _ in range(H*2)]
M=[[abs(A[i][j]-A[H+i][j]) for j in range(W)] for i in range(H)]
m=max(max(j for j in i) for i in M)
r=m*(H+W)+1
dp=np.zeros((H,W,r),dtype='bool')
dp[0][0][M[0][0]]=True
it = itertools.product(range(H),range(W))
next(it)
for h,w in it:
    m=M[h][w]
    dp[h][w][m:] |= dp[h][w-1][:r-m] | dp[h-1][w][:r-m]
    dp[h][w][:r-m] |= dp[h][w-1][m:] | dp[h-1][w][m:]
    dp[h][w][:m] |= dp[h][w-1][m:0:-1] | dp[h-1][w][m:0:-1]

for i in range(r):
    if dp[-1][-1][i]:
        print(i)
        break
