import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
import numpy as np

INF = 2**30
n = int(input())
P = tuple(map(int, input().split()))
T = [[] for _ in range(n)]
for i, p in enumerate(P, 1):
  T[p-1].append(i)
X = tuple(map(int, input().split()))
D = [-1]*n
def dfs(v):
  if D[v] != -1:
    return D[v]
  l = len(T[v])
  x = X[v]
  dp = np.full(x+1, INF, dtype=np.int64)
  dp[0] = 0
  for i, nv in enumerate(T[v]):
    k = np.full(x+1, INF, dtype=np.int64)
    d = dfs(nv)
    if x+1 >= X[nv]:
      np.minimum(k[X[nv]:], dp[:x+1-X[nv]]+d, out=k[X[nv]:])
    if x+1 >= d:
      np.minimum(k[d:], dp[:x+1-d]+X[nv], out=k[d:])
    dp = k.copy()
  res = dp.min()
  D[v] = res
  return res
ans = dfs(0)
if ans == INF:
  print("IMPOSSIBLE")
else:
  print("POSSIBLE")
