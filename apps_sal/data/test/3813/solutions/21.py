from collections import Counter
n = int(input())
p = [0,0]+list(map(int,input().split()))
xls = [0]+list(map(int,input().split()))
dp = [[] for i in range(n+1)]
stack = []
cp = Counter(p)
deg = [cp[i] for i in range(n+1)]
def dp_sol(ls,s):
  l = len(ls)
  mnsm = sum(list(zip(*ls))[0])
  totsm = sum([sum(i) for i in ls])
  if mnsm > s:
    return 10**18
  dp = [[0 for i in range(s+1)] for j in range(l+1)]
  dp[0][0] = 1
  for i in range(1,l+1):
    mn,mx = ls[i-1]
    for j in range(mn,s+1):
      dp[i][j] |= dp[i-1][j-mn]
    for j in range(mx,s+1):
      dp[i][j] |= dp[i-1][j-mx]
  for i in range(s,-1,-1):
    if dp[l][i]:
      return totsm-i
for i in range(1,n+1):
  if cp[i] == 0:
    stack.append(i)
while stack:
  x = stack.pop()
  a = 0
  px = p[x]
  if dp[x]:
    a = dp_sol(dp[x],xls[x])
    if a == 10**18:
      print("IMPOSSIBLE")
      return
  if a < xls[x]:
    dp[px].append((a,xls[x]))
  else:
    dp[px].append((xls[x],a))
  deg[px] -= 1
  if deg[px] == 0:
    stack.append(px)
print("POSSIBLE")
