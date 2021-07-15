import math
n=int(input())
a=int(math.sqrt(n))
ans=4*a
n=n-a*a
ans+=2*math.ceil(n/a)
print(ans)

