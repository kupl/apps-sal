import sys
sys.setrecursionlimit(100000000)
N, K = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(N-1)]
graph = [[] for _ in range(N)]
used = [-1]*N
ans = K
mod = 10**9+7

for a, b in ab:
  a -= 1
  b -= 1
  graph[a] += [b]
  graph[b] += [a]


def npr(n, r, p):
  e = 1
  for i in range(n, n-r, -1):
    e *= i
    e %= p

  return e

def dfs(u, pre):
  nonlocal ans
  child = 0
  for v in graph[u]:
    if v != pre:
      dfs(v, u)
      child += 1
  if u == 0:
    ans *= npr(K-1, child, mod)
  else:
    ans *= npr(K-2, child, mod)

  ans %= mod

dfs(0, -1)
print(ans)

