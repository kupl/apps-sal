import math
N = int(input())

ans = 1
for i in range(1,math.floor(math.sqrt(N))+1):
  if i * i <= N:
    ans = i * i
    
print(ans)
