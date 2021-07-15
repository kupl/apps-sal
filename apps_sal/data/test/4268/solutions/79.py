n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
ans = 0
from math import sqrt
for i in range(n):
  for j in range(i+1,n):
    dis = 0
    for k in range(d):
      dis += (x[i][k]-x[j][k])**2
    if sqrt(dis) == int(sqrt(dis)):
      ans += 1
print(ans)
