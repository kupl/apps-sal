import sys
sys.setrecursionlimit(100000)

MOD = 10**9 + 7
N, K = map(int,input().split())

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    a, b = a-1, b-1

    G[a].append(b)
    G[b].append(a)

# 頂点nowを根とする部分木の色の塗り方 (parが親の時)
#   ただしnowはすでに塗られているとする
def dfs(now, par):
    if K < len(G[now]): return 0

    res = 1

    if par == -1:
        colors = K-1
        for i in range(len(G[now])):
            res *= colors-i
            res %= MOD
    else:
        colors = K-2
        for i in range(len(G[now])-1):
            res *= colors-i
            res %= MOD

    for c in G[now]:
        if c == par: continue
        
        res *= dfs(c, now)
        res %= MOD
    
    return res

print(K * dfs(0,-1) % MOD)
