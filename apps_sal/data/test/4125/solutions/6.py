N,X = map(int,input().split())
x = list(map(int,input().split()))
ans = 0
from math import gcd
for i in range(N):
  ans = gcd(ans,abs(X-x[i]))
print(ans)
