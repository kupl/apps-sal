MOD=10**9+7
L=input()
N=len(L)
ans,lbit=0,0
for i in range(N):
    if L[i]=='0':
        continue
    ans=(ans+(pow(3,N-i-1,MOD)*pow(2,lbit,MOD)%MOD))%MOD
    lbit+=1
print((ans+pow(2,lbit,MOD))%MOD)
