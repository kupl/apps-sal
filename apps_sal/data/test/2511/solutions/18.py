import sys
sys.setrecursionlimit(10 ** 6)
N,K=map(int,input().split())
tree=[[]for _ in range(N+1)]
MOD=10**9+7
ans=K
enuk=[1]*(N)
for i in range(N-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    enuk[i+1]=(enuk[i]*(K-2-i))%MOD
def dfs(a,b):
    if a==1:
        node=len(tree[a])
        ret=1
        for i in range(node):
            ret*=K-1-i
            ret%=MOD
    else:
        node=len(tree[a])-1
        ret=enuk[node]%MOD
    for i in tree[a]:
        if i==b:
            continue
        ret=ret*dfs(i,a)%MOD
    return ret
ans*=dfs(1,0)
print(ans%MOD)
