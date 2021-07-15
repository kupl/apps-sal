import math
n=int(input())
 
ans=n
k=math.ceil(((n*8+9)**(1/2) - 1)/2) - 1

while k*(k+1) <= 2*(n+1):
  k += 1

ans -= k-2
 
print(ans)
