from collections import defaultdict as dd
mod = pow(10, 9) + 7
"""
def dfs_visit(V,adj,s,c):
    for v in adj[s]:
        if v not in parent:
            parent[v]=s
            c=c+1
            dfs_visit(V,adj,v,c)
    return(c)
            
def dfs(V,adj):
    ans=[]
    for s in V:
        if s not in parent:
            parent[s]=None
            c=dfs_visit(V,adj,s,1)
            ans.append(c)
    return(ans)
"""


def bfs(s, adj):
    nonlocal parent
    t = 1
    # print("df",s)
    frontier = [s]
    while frontier:
        nex = []
        for u in frontier:
            for v in adj[u]:
                if v not in parent:
                    # print(v)
                    t += 1
                    parent.add(v)
                    nex.append(v)
        frontier = nex
    return(t)


adj = dd(list)
n, k = [int(i) for i in input().split(' ')]
for ii in range(n - 1):
    x, y, h = [int(i) for i in input().split(' ')]
    if h == 0:
        adj[x].append(y)
        adj[y].append(x)

V = [i + 1 for i in range(n)]
parent = set()

fk = []
for i in V:
    if i not in parent:
        parent.add(i)
        tr = bfs(i, adj)
        # print(i,tr)
        fk.append(tr)
# print(fk)
ans = pow(n, k, mod)
for i in fk:
    ans = (ans - pow(i, k, mod)) % mod
print(ans % mod)
