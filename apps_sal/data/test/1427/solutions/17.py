import fractions
mod=10**9+7
def lcm(m,n):return m//fractions.gcd(m,n)*n
n=int(input())
a=list(map(int,input().split()))
l=a[0]
ans=0
for i in a:l=lcm(i,l)
for i in a:ans+=l*pow(i,mod-2,mod)%mod
print(ans%mod)
