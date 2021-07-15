import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
import numpy as np

INF = 2**30
n = int(input())
P = list(map(int, input().split()))
T = [[] for _ in range(n)]
for i, p in enumerate(P, 1):
  T[p-1].append(i)
X = list(map(int, input().split()))
D = [[-1]*n for _ in range(2)]
def dfs(color, v):
  if D[color][v] != -1:
    return D[color][v]
  l = len(T[v])
  x = X[v]
  dp = np.full(x+1, INF, dtype=np.int64)
  dp[0] = 0
  for i, nv in enumerate(T[v]):
    k = np.full(x+1, INF, dtype=np.int64)
    if x+1 >= X[nv]:
      np.minimum(k[X[nv]:], dp[:x+1-X[nv]]+dfs(color, nv), out=k[X[nv]:])
    if x+1 >= dfs(color^1, nv):
      np.minimum(k[dfs(color^1, nv):], dp[:x+1-dfs(color^1, nv)]+X[nv], out=k[dfs(color^1, nv):])
    dp = k.copy()
  res = dp.min()
  D[color][v] = res
  return res
ans = dfs(0, 0)
if ans == INF:
  print("IMPOSSIBLE")
else:
  print("POSSIBLE")
