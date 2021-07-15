mod = pow(10,9)+7
n,k = map(int,input().split())
inv = [0,1]
fact = [1,1]
ifact = [1,1]
for i in range(2,n+1):
    inv.append(inv[mod%i]*(mod-mod//i)%mod)
    fact.append(i*fact[-1]%mod)
    ifact.append(ifact[-1]*inv[i]%mod)

def combi(a,b):
    if a >= b:
        return fact[a]*ifact[b]*ifact[a-b]%mod
    else:
        return 0

for i in range(1,k+1):
    print(combi(n-k+1,i)*combi(k-1,i-1)%mod)
