import math
N=int(input())
ans=N
for i in range(N):
  if math.sqrt(ans).is_integer():
    print(ans)
    break
  ans-=1
