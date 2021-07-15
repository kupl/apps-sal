n, k = [int(i) for i in input().split()]
adj = [[] for i in range(n+1)]

ans = 0
# no of good paths = all paths - non-good paths
# = all paths - paths where no blacks

par = [i for i in range(n+1)]

def find(i):
    nonlocal par
    if par[i] == i:
        return i
    par[i] = find(par[i])
    return par[i]

def unite(i, j):
    nonlocal par
    if find(i) < find(j):
        i, j = j, i
    par[find(i)] = find(j)

for i in range(n-1):
    u, v, c = [int(i) for i in input().split()]
    adj[u].append((v,c))
    adj[v].append((u, c))
    if c==0:
        unite(u, v)

sz = [0 for i in range(n+1)]
for i in range(1, n+1):
    sz[find(i)] += 1
grps = []
for i in range(1, n+1):
    if find(i) == i:
        grps.append(i)
        
mod = 10**9 + 7
ans += pow(n, k, mod) #n**k

for i in grps:
    ans -= pow(sz[i], k, mod) #sz[i]**k
    ans += mod
print(ans%mod)

