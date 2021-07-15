from collections import defaultdict
n=int(input())
a=[int(i) for i in input().split()]
INF=float('inf')
dp0=defaultdict(lambda: -INF)
dp1=defaultdict(lambda: -INF)
dp0[(0,0)]=0
for i in range(1,n+1):
  for j in range(i//2-1,(i+1)//2+1):
    dp0[(i,j)]=max(dp0[(i-1,j)],dp1[(i-1,j)])
    dp1[(i,j)]=dp0[(i-1,j-1)]+a[i-1]
print(max(dp0[(n,n//2)],dp1[(n,n//2)]))
