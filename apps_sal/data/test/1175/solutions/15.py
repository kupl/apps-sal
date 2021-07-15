L,R = map(int,input().split())

mod = 10**9+7
m = 64 +1
fac = [1]*m
ninv = [1]*m
finv = [1]*m
for i in range(2,m):
    fac[i] = fac[i-1]*i%mod
    ninv[i] = (-(mod//i)*ninv[mod%i])%mod
    finv[i] = finv[i-1]*ninv[i]%mod

def comb(n,k):
    return (fac[n]*finv[k]%mod)*finv[n-k]%mod

def f(N):
    if N==0:return 0
    S = bin(N)[2:]
    L = len(S)
    ret = pow(2,S.count("1")-1,mod)
    for i in range(L):
        if S[i] == "0" : continue
        c = S[:i].count("1")
        j = max(0,L-i-1)
        for k in range(j+1):
            if c+k == 0 : continue
            ret += pow(2,c+k-1,mod)*comb(j,k)
            ret %= mod
    return ret

def g(R,L):
    if L==0 : return 0
    Nr = len(bin(R))-2
    Nl = len(bin(L))-2
    if Nr!=Nl :
        R = int("1"*Nl,2)
        Nr = Nl
    ret = f(int("0"+"1"*(Nr-1),2))
    
    R = bin(R)[2:]
    L = bin(L)[2:]
    for i in range(Nr):
        if R[i] == "0": continue
        if i==0 : R2 = R
        else: R2 = R[:i] + "0" + "?"*(Nr-i-1)
        for j in range(Nl):
            if L[j] == "0" : continue
            if j==0 : L2 = L
            else: L2 = L[:j] + "0" + "?"*(Nl-j-1)
            tmp = 1
            for r,l in zip(R2,L2):
                if r==l=="?" : tmp *= 3
                if r=="?" and l=="0" : tmp *= 2
                if r=="1" and l=="?" : tmp *= 2
                if r=="0" and l=="1" : tmp *= 0
                tmp %= mod
            ret += tmp
    return ret

print((f(R)-g(R,L-1))%mod)
