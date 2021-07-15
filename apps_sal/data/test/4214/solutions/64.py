import math


n = int(input())
t = [list(map(int,input().split())) for i in range(n)]
ans = 0

for i in range(n):
  x, y = t[i]
  for j in range(i, n):
    x1, y1 = t[j]
    ans += math.sqrt((x-x1)**2 + (y-y1)**2)*(n-1)*2
print(ans/((n-1)*n))
