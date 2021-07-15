import numpy as np
import  itertools
N=int(input())
XY=[]
for _ in range(N):
  x, y = list(map(int, input().split()))
  XY.append([x,y])

D=np.zeros((N, N))
for i in range(N-1):
  xi, yi=XY[i][0], XY[i][1]
  for j in range(i+1, N):
    xj, yj=XY[j][0], XY[j][1]
    distance=np.sqrt((xi-xj)**2 + (yi-yj)**2)
    D[i][j]=distance
    D[j][i]=distance

ans=0
for l in itertools.permutations(list(range(N))):
  dis=0
  for i in range(N-1):
    dis+=D[l[i]][l[i+1]]
  ans+=dis
print((ans/np.math.factorial(N)))


