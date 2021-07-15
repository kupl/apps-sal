from numpy import array
from numpy.linalg import norm
n,d=map(int,input().split())
X = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n-1):
  for j in range(i+1,n):
    if norm(array(X[i])-array(X[j])).is_integer():
      ans += 1
print(ans)
