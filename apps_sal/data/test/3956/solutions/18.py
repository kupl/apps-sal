mod=998244353
k,n=map(int,input().split())

def modinv(n):
    return pow(n,mod-2,mod)
m=n+k
Fact=[1]
for i in range(1,m+1):
    Fact.append(Fact[i-1]*i%mod)
Finv=[0]*(m+1)
Finv[-1]=modinv(Fact[-1])
for i in range(m-1,-1,-1):
    Finv[i]=Finv[i+1]*(i+1)%mod
def comb(n,r):
    if r<0 or n<r:
        return 0
    return Fact[n]*Finv[r]*Finv[n-r]%mod
def hcomb(n,r):
    return comb(n+r-1,r)
Pow=[1]*(k+1)
for i in range(k):
    Pow[i+1]=Pow[i]*2%mod
def solve(x):
    ret=0
    if x%2:
        p=x//2
        for q in range(p+1):
            ret+=Pow[q]*comb(p,q)*hcomb(k-2*p+q,n-q)
            ret%=mod
    else:
        p=x//2-1
        for q in range(p+1):
            ret+=Pow[q]*comb(p,q)*(hcomb(k-2*p+q-1,n-q)+hcomb(k-2*p+q-1,n-q-1))
            ret%=mod
    return ret
Ans=[]
for i in range(2,k+2):
    Ans.append(solve(i))
print(*Ans,sep='\n')
print(*reversed(Ans[:k-1]),sep='\n')
