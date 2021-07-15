import numpy as np
H,W = map(int,input().split())
HL=list(range(H))
WL=list(range(W))
Gd = np.array([list(input()) for _ in HL])
Gd = np.where(Gd=='.', 1, 0)
L=np.zeros((H,W),dtype=np.int64)
R=np.zeros((H,W),dtype=np.int64)
U=np.zeros((H,W),dtype=np.int64)
D=np.zeros((H,W),dtype=np.int64)

for w in WL:
  R[:,w]=(R[:,w-1]+1)*Gd[:,w]
  L[:,-w-1]=(L[:,-w]+1)*Gd[:,-w-1]
for h in HL:
  D[h,:]=(D[h-1,:]+1)*Gd[h,:]
  U[-h-1,:]=(U[-h,:]+1)*Gd[-h-1,:]
print(np.max(D+U+L+R-3))
