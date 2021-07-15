import math
n=int(input())
ans=0
for i in range(1,n+1):
    for j in range(1,n+1):
        r=math.gcd(i,j)
        for k in range(1,n+1):
            ans+=math.gcd(r,k)
print(ans)
