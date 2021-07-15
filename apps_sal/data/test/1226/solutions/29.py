n,a,b = map(int,input().split())
p = 10**9 + 7
def CC(n,k):
  X,Y = 1,1
  for i in range(n-k+1,n+1):
    X = X*i%p
  for j in range(1,k+1):
    Y = Y*j%p
  YY = pow(Y,p-2,p)
  return(X*YY%p)
A = CC(n,a)
B = CC(n,b)
ALL = pow(2,n,p)
ans = (ALL-1-A-B)%p
print(ans)
