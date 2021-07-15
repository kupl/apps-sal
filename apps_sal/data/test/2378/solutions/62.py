import sys
sys.setrecursionlimit(10**6)

readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: list(map(int, readline().split()))
nl = lambda: list(map(int, readline().split()))


n = ni()
G = [list() for _ in range(n)]
for _ in range(n-1):
  a, b = nm()
  a -= 1; b -= 1
  G[a].append(b)
  G[b].append(a)
  
  
mod = 10**9 + 7
dub = [1]*(n+1)
for i in range(n):
  dub[i+1] = dub[i] * 2
  if dub[i+1] > mod:
    dub[i+1] -= mod
    
size = [1]*n
def dfs_depandsize(tree,v,p):
    for x in tree[v]:
        if x == p:
            continue
        size[v] += dfs_depandsize(tree,x,v)
    return size[v]
dfs_depandsize(G, 0, -1)
ans = 0
for v in range(n):
  c = 0
  res = 1
  for x in G[v]:
    if size[x] < size[v]:
      c += size[x]
      res += dub[size[x]] - 1
  res += dub[n-1-c] - 1
  res %= mod
  ans = (ans + dub[n-1] - res) % mod
print((ans * pow(dub[n], mod-2, mod) % mod))

