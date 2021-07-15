import numpy as np
N = int(input())
XY = np.array([list(map(int,input().split())) for _ in [0]*N])
th = np.arctan2(XY[:,1],XY[:,0])
XY = XY[th.argsort()]
ans = 0
n = np.linalg.norm
s = np.sum
for i in range(N):
    for j in range(i+1,i+N+1):
        r = n(s(XY[i:j],axis=0)+s(XY[:max(0,j-N)],axis=0))
        ans = max(ans,r)
print(ans)
