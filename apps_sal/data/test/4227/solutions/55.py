n,m = map(int,input().split())
visit = [False]*n
r = [[] for _ in range(n)]
for i in range(m):
  a,b = map(lambda x:int(x)-1,input().split())
  r[a].append(b)
  r[b].append(a)
def dfs(x,v):
  if v[x]:
    return
  v = list(v)
  v[x] = True
  if all(v):
    nonlocal ans
    ans += 1
    return
  for y in r[x]:
    dfs(y,v)
ans = 0
dfs(0,[False]*n)
print(ans)
