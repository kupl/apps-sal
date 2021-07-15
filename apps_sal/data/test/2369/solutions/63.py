n,k=list(map(int,input().split()))
a=sorted(list(map(int,input().split())))
mod=10**9+7

def fact(n,mod):
    a=[[] for _ in range(n+1)]
    a[0]=1
    for i in range(n):
        a[i+1]=(a[i]*(i+1))%mod
    return a
f=fact(n,mod)
g=[]
for i in range(n+1):
    g.append(pow(f[i],-1,mod))
def com(n,r):
    return f[n]*g[r]*g[n-r]
ans=0
for i in range(n-k+1):
    ans=ans+(a[-i-1]-a[i])*com(n-i-1,k-1)
print((ans%mod))

