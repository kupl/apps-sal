import sys
sys.setrecursionlimit(1000000000)
n,k = map(int,input().split())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

mod = 1000000007
def perm(n,k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n]*finv[n-k]%mod
fac = [1]*(k+1)
finv = [1]*(k+1)
for i in range(1,k+1):
    fac[i] = fac[i-1]*i%mod
    finv[i] = pow(fac[i],mod-2,mod)

def dfs(cur,prev=-1):
    nxtcnt = 0
    res = 1
    for nxt in G[cur]:
        if nxt == prev: continue
        nxtcnt += 1
        res = res*dfs(nxt,cur)%mod
    colors = k-1 if cur == 0 else k-2
    res = res*perm(colors,nxtcnt)%mod
    return res
  
ans = k*dfs(0)%mod
print(ans)
