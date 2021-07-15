import math
N = list(map(int,input().split()))
xy = [map(int, input().split()) for _ in range(N[0])]
X, Y = [list(i) for i in zip(*xy)]
cnt = 0
for i in range(N[0]):
  if( math.sqrt(X[i]**2 + Y[i]**2) <= N[1] ):
    cnt = cnt +1
print(cnt)
