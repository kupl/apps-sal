import sys
input = sys.stdin.readline

N,M=map(int,input().split())
mod=10**9+7

FACT=[1]
for i in range(1,5*10**5+1):
    FACT.append(FACT[-1]*i%mod)

FACT_INV=[pow(FACT[-1],mod-2,mod)]
for i in range(5*10**5,0,-1):
    FACT_INV.append(FACT_INV[-1]*i%mod)

FACT_INV.reverse()

def Combi(a,b):
    if 0<=b<=a:
        return FACT[a]*FACT_INV[b]*FACT_INV[a-b]%mod
    else:
        return 0

ANS=0
for i in range(N+1):
    if i%2==0:
        ANS=(ANS+Combi(N,i)*FACT[M-i]*FACT_INV[M-N])%mod
    else:
        ANS=(ANS-Combi(N,i)*FACT[M-i]*FACT_INV[M-N])%mod

print(ANS*FACT[M]*FACT_INV[M-N]%mod)
