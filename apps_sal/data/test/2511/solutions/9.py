import sys 
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
    
mod = 10**9 + 7
def P(x,y):
    # x = k - 2
    # y = n - 1
    cnt = 0
    ans = 1
    waru = 1
    while cnt < y:
        ans *= (x-cnt)
        ans %= mod
        cnt += 1
    return ans%mod


ans = 1
def dfs(v,p):
    nonlocal ans
    us = edges[v]
    for u in us:
        if u == p: continue
        if len(edges[u]) == 1: ans *= 1
        ans *= P(k-2, len(edges[u])-1)   
        ans %= mod
        dfs(u,v)

dfs(0,-1)
n0 = len(edges[0])
a = P(k,n0+1)
# print(n0,a)
ans *= a
ans %= mod
print(ans)
