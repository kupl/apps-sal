import sys
sys.setrecursionlimit(10**7)
n,k = map(int,input().split())
li = [[] for _ in range(n+1)]
mod = 10**9+7
ans = k
perm = [1]*(n)# 組み合わせ(k-2)P(要素)

for i in range(n-1):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
    perm[i+1] = (perm[i]*(k-2-i))%mod

def dfs(now,before):
    point = 1
    if now == 1:
        ret = 1
        ko = len(li[1])
        for i in range(ko):
            ret *= k-1-i
            ret %= mod
    else:
        ko = len(li[now])-1
        ret= perm[ko]%mod
    
    for i in li[now]:
        if i==before:
            continue
        ret = ret*dfs(i,now)%mod
    return ret

ans *= dfs(1,0)

print(ans%mod)
