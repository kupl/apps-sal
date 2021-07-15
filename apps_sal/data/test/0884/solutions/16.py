f=[1]*50001
mod=998244353
for i in range(1,5001):
    f[i]=(f[i-1]*i)%mod
a,b,c=(int(i) for i in input().split())
def pwr(b,e):
    if(b==0): return 0
    if(e==0): return 1
    if(e%2==0):
        z=pwr(b,e/2)%mod
        return (z*z)%mod
    return (b*pwr(b,e-1))%mod
def nCr(n,r):
    den=(f[r]*f[n-r])%mod
    return (f[n]*pwr(den,mod-2))%mod
def g(x,y):
    mn=min([x,y])
    sm=0
    nonlocal mod
    for i in range(0,mn+1):
        sm+=(nCr(x,i)*nCr(y,i)*f[i])%mod
        sm=sm%mod
    return sm
ans=g(a,b)*g(b,c)*g(c,a)
ans=ans%mod
print(int(ans))
    

