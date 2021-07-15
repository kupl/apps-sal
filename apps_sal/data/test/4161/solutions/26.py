import math
k=int(input())
ans=0
for a in range(1,k+1):
    for b in range(1,k+1):
        if math.gcd(a,b)==1:
            ans+=k
        else :
            for c in range(1,k+1):
                ans+=math.gcd(math.gcd(a,b),c)
print(ans)

