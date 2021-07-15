# E - NEQ
import sys
sys.setrecursionlimit(10**6)
MOD = 10**9+7
mon_l = dict({})

def mon(m,n):
    if (m,n) in mon_l:
        return mon_l[(m,n)]
    if n==1:
        mon_l[(m,n)] = m-1
        return mon_l[(m,n)]
    if n==2:
        mon_l[(m,n)] = ((m-1)+(m-2)**2)%MOD
        return mon_l[(m,n)]
    else:
        mon_l[(m,n)] = ((n-1)*(mon(m-1,n-1)+mon(m-2,n-2)) + (m-n)*mon(m-1,n-1))%MOD
        return mon_l[(m,n)]
    
def permu(m,n):
    ans = 1
    for _ in range(n):
        ans = m*ans%MOD
        m -= 1
    return ans

N,M = map(int,input().split())
ans = permu(M,N)*mon(M,N)%MOD
print(ans)
