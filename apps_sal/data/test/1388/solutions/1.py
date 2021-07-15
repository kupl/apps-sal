import sys
input = sys.stdin.readline
n = int(input())
cbc = [list(map(int,input().split())) for i in range(n)]
ab = [list(map(int,input().split())) for i in range(n-1)]
graph = [[] for i in range(n+1)]
if n == 1:
  if cbc[0][1] != cbc[0][2]:
    print(-1)
  else:
    print(0)
  return
deg = [0]*(n+1)
for a,b in ab:
  graph[a].append(b)
  graph[b].append(a)
  deg[a] += 1
  deg[b] += 1
deg[1] += 1
stack = [1]
par = [0]*(n+1)
par[1] = -1
leaf = []
while stack:
  x = stack.pop()
  if x != 1 and len(graph[x]) == 1:
    leaf.append(x)
  for y in graph[x]:
    if par[y]:
      continue
    par[y] = x
    cbc[y-1][0] = min(cbc[y-1][0],cbc[x-1][0])
    stack.append(y)
dp = [[0,0] for i in range(n+1)]
ans = 0
while leaf:
  x = leaf.pop()
  p = par[x]
  if cbc[x-1][1] != cbc[x-1][2]:
    if cbc[x-1][1] == 1:
      dp[x][0] += 1
    else:
      dp[x][1] += 1
  if min(dp[x][0],dp[x][1]):
    if dp[x][0] > dp[x][1]:
      dp[x][0] -= dp[x][1]
      ans += cbc[x-1][0]*dp[x][1]*2
      dp[x][1] = 0
    else:
      dp[x][1] -= dp[x][0]
      ans += cbc[x-1][0]*dp[x][0]*2
      dp[x][0] = 0
  dp[p][0] += dp[x][0]
  dp[p][1] += dp[x][1]
  deg[p] -= 1
  if deg[p] == 1:
    leaf.append(p)
if dp[1][0] != dp[1][1]:
  print(-1)
else:
  print(ans)
