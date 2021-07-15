H,W=list(map(int,input().split()))
import numpy as np
m=np.array([[0 if i=="#" else 1 for i in input()] for i in range(H)])
l,r,u,d=np.zeros((4,H,W))
for i in range(H):
   u[i]=(u[i-1]+1)*m[i]
   d[-i-1]=(d[-i]+1)*m[-i-1]
for i in range(W):
   r[:,i]=(r[:,i-1]+1)*m[:,i]
   l[:,-i-1]=(l[:,-i]+1)*m[:,-i-1]
print(int(np.max(u+r+l+d))-3)
