import sys
sys.setrecursionlimit(200000)

mod = 10**9 +7
N,K = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(cur,p,nei):
    #curにいる状態で、選べる色がcandi通りある場合の、塗り方の場合の数。
    #pが親,neiがcurの距離2以下のノードの数（curの子、弟ノードは除く）。neiが0,1のとき子に渡すneiはnei+1+兄の数、
    # neiが2のとき、子に渡すneiは、2+兄の数。
    res = K-nei 
    nxnei = min(nei+1,2)
    for nx in edges[cur]:
        if nx != p:
            res = res * dfs(nx,cur,nxnei) % mod
            nxnei += 1
    return res

print(dfs(1,0,0))
