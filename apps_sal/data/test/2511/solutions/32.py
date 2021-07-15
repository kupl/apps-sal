import sys
sys.setrecursionlimit(10**7)

MOD=10**9+7

N,K=list(map(int,input().split()))
g=[[] for _ in range(N)]
for i in range(N-1):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

MAX=10**6
fc=[1]*MAX
inv=[1]*MAX
ifc=[1]*MAX

for i in range(2,MAX):
    fc[i]=i*fc[i-1]%MOD
    inv[i]=MOD-(MOD//i)*inv[MOD%i]%MOD
    ifc[i]=inv[i]*ifc[i-1]%MOD

def comb(n,k):
    if n<0 or k<0 or n-k<0:
        return 0
    return fc[n]*ifc[n-k]%MOD*ifc[k]%MOD

def dfs(cur,par):
    ret=1
    ch=len(g[cur])
    if par!=-1:
        ch-=1
    
    if par==-1:
        ret=comb(K-1,ch)*fc[ch]%MOD
    else:
        ret=comb(K-2,ch)*fc[ch]%MOD
        
        
    for dst in g[cur]:
        if dst==par:
            continue
        ret=ret*dfs(dst,cur)%MOD
    return ret

ans=K*dfs(0,-1)%MOD
print(ans)

