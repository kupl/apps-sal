import math
n,x=map(int, input().split())
a=[int(x) for x in input().split()]

ans=abs(x-a[0])
for i in range(1,n):
    ans=math.gcd(abs(x-a[i]),ans)

print(ans)
