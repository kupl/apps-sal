import numpy as np

H,W=map(int,input().split())
S=np.array([list(input()) for _ in range(H)]) == "."

ups=np.zeros((H,W),dtype=int)
downs=np.zeros((H,W),dtype=int)
rights=np.zeros((H,W),dtype=int)
lefts=np.zeros((H,W),dtype=int)

for i in range(1,H):
    ups[i,:]=(ups[i-1,:]+1)*S[i-1,:]

for i in range(H-2,-1,-1):
    downs[i,:]=(downs[i+1,:]+1)*S[i+1,:]

for i in range(1,W):
    rights[:,i]=(rights[:,i-1]+1)*S[:,i-1]

for i in range(W-2,-1,-1):
    lefts[:,i]=(lefts[:,i+1]+1)*S[:,i+1]

ans=((ups+downs+lefts+rights)*S).max()+1
print(ans)
