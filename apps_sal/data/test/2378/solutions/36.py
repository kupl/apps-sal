import sys
sys.setrecursionlimit(10**6)

N = int(input())
adj = [ [] for _ in range(N+1) ]
for _ in range(N-1):
  a,b = map(int,input().split())
  adj[a].append(b)
  adj[b].append(a)

def dfs(v, p=-1):
  nonlocal ans

  res = 1
  ts = []
  for u in adj[v]:
    if (u==p): continue
    t = dfs(u,v)
    res += t
    ts.append(t)

  if p != -1:
    ts.append(N-res)

  # print(v, ts)

  # now = pow(2, N-1, MOD)-1
  now = pows[N-1]-1
  for t in ts:
    # now -= pow(2, t, MOD)-1
    now -= pows[t] - 1
  ans += now
  return res

ans = 0
MOD = 10**9+7
# 高速化1
pows = [1] * (N+1)
for i in range(1, N+1):
  pows[i] = (pows[i - 1] * 2) % MOD

dfs(1)
print((ans * pow(pows[N], MOD-2, MOD)) % MOD)
