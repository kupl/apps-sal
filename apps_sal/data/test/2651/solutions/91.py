N,M = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

## 0,x1,x2,x3
## S = (x1 + x2 + x3 + (x2-x1) + (x3-x1) + (x3-x2)) * ...
##.  = (3*x3 + x2 - x1 - 3* 0)
##.  = ((3-0) + (2-1) + (1-2) + (0-3)
mod = int(1e9+7)
X.sort(reverse=True)
Y.sort(reverse=True)
XP,YP = 0,0
for i in range(N):
  XP += (N-1-i*2) * X[i] 
  XP %= mod
for i in range(M):
  YP += (M-1-i*2) * Y[i] 
  YP %= mod
  
print(((XP * YP)%mod))

