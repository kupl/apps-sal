from math import gcd
k=int(input())
ans=0
for i in range(1,k+1):
    for j in range(1,k+1):
        ans_=gcd(i,j)
        for l in range(1,k+1):
            ans+=gcd(ans_,l)
print(ans)
