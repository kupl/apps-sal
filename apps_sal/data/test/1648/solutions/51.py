import math
def com(n,r):
  return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))
n,k=map(int,input().split())
for i in range(1,k+1):
  if n-k+1<i:
    print(0)
  else:
    print(com(k-1,i-1)*com(n-k+1,i)%(10**9+7))
