# E - Colorful Blocks
import sys
sys.setrecursionlimit(10**8)

MOD = 998244353
N,M,K = map(int,input().split())
inv_M = pow(M-1,-1,MOD) if M>1 else 0
ans = 0
tmp = pow(M-1,N-1,MOD) if M>1 else 0
comb = 1
for i in range(K+1):
    ans = (ans+M*comb*tmp)%MOD
    if i==K:
        break
    tmp = (tmp*inv_M)%MOD
    comb = (comb*(N-1-i)*pow(i+1,-1,MOD))%MOD
if M==1 and K==N-1:
    ans += 1
print(ans)
