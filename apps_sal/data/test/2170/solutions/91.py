mod = pow(10,9)+7
n,m = map(int,input().split())
ans = 0
inv = [0,1]
fact = [1,1]
ifact = [1,1]
for i in range(2,m+1):
    inv.append(inv[mod%i]*(mod-int(mod/i))%mod)
    fact.append(i*fact[-1]%mod)
    ifact.append(ifact[-1]*inv[i]%mod)

def combi(a,b):
    return fact[a]*ifact[b]*ifact[a-b]%mod
def permi(a,b):
    return fact[a]*ifact[a-b]%mod

for i in range(n+1):
    now = combi(n,i)
    now *= permi(m-i,n-i)
    now %= mod
    ans += now*(-1)**(i&1)
    ans %= mod
ans *= permi(m,n)
ans %= mod
print(ans)
