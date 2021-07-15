from copy import *

N=int(input())
X=list(map(int,input().split()))
Y=deepcopy(X)
Y.sort()
mid1=Y[N//2-1]
mid2=Y[N//2]
for i in range(N):
  if X[i]<=mid1:
    print(mid2)
  else:
    print(mid1)

