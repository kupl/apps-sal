import math
n,k = map(int, input().split())
s = 0
ans = 0
for x in range(1,n+1):
  if x >= k:
    a = 0
  else:
    a = math.ceil(math.log2(k/x))
  b = (1 / n) * ((0.5) ** a)  
  ans += b
  
   
print(ans)
