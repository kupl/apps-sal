import math
N = int(input())
ans = 0
for i in range(N):
  if i == 0:
    ans = int(input())
  else:
    a = int(input())
    ans = (a * ans) // math.gcd(ans,a)
print(ans)

