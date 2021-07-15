# F - Strivore
import sys
MOD = 10**9+7
K = int(input())
S = input()
l = len(S)
ans = 0
 
tmp = pow(26,K,MOD)
ans = tmp
waru = pow(26,-1,MOD)
 
for i in range(1,K+1):
    tmp = (tmp*25*waru)%MOD
    tmp = (tmp*(l-1+i)*pow(i,-1,MOD))%MOD
    ans = (ans+tmp)%MOD
 
print(ans)
