n,a,b=map(int,input().split())

mod=10**9+7
def modpow(a,n):
    if n<1:
        return 1
    ans=modpow(a,n//2)
    ans=(ans*ans)%mod
    if n%2==1:
        ans*=a
    return ans%mod
    
def cmb(n,i):#逆元
    inv,ans=1,1
    for j in range(1,i+1):
        ans=ans*(n-j+1)%mod
        inv=inv*j%mod
    return (ans*modpow(inv,mod-2))%mod



ans_n=pow(2,n,mod)-1
ans_a=cmb(n,a)%mod
ans_b=cmb(n,b)%mod

print((ans_n-ans_a-ans_b)%mod)
