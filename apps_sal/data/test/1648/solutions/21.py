import math
def comb(n, r):
  if n-r>=0:
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
  else:
    return 0

n,k=map(int, input().split())
for i in range(1,k+1):
  print(comb(n-k+1,i)*comb(k-1,i-1)%(10**9+7))
