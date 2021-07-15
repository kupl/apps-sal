import fractions
N=int(input())
A=list(map(int,input().split()))
MOD=10**9+7
ans=1
gcd=A[0]
for i in range(1,N):
    a=A[i]
    b=fractions.gcd(a,gcd)
    temp=gcd
    gcd=temp*a//b
    ans=ans*(a//b)+temp//b
    ans%=MOD
print(ans)
