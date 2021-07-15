from fractions import gcd
n=int(input())

ans=0
for i in range(n,max(0,n-101),-1):
    for j in range(i,max(0,n-101),-1):
        for k in range(j,max(0,n-101),-1):
            x=(i*j)//gcd(i,j)
            x=(x*k)//gcd(x,k)
            ans=max(ans,x)
print(ans)

