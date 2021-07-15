def sarch(i,j):
    cnt=0
    i1=[i-1,i,i+1]
    j1=[j-1,j,j+1]
    for x in range(3):
        for y in range(3):
            if S[i1[x]][j1[y]]=="#":
                cnt+=1
    return cnt

import numpy as np
H,W=map(int,input().split())
S=np.array([list(str(input())) for i in range(H)])


gyo_0=np.array(["."]*W)
retu_0=np.array([["."]]*(H+2))

S=np.vstack((gyo_0,S))
S=np.vstack((S,gyo_0))
S=np.hstack((retu_0,S))
S=np.hstack((S,retu_0))

for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j]==".":
            S[i][j]=sarch(i,j)
        print(S[i][j],end="")
    print()
