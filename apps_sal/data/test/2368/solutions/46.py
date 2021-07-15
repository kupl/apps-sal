from collections import deque
n,m = map(int,input().split())
a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
  i,j = map(lambda x:int(x)-1,input().split())
  g[i].append(j)
  g[j].append(i)
c = [False]*n
ans = "Yes"
for i in range(n):
  if c[i]:
    continue
  c[i] = True
  da = a[i]
  db = b[i]
  q = deque(g[i])
  while(q):
    j = q.popleft()
    if c[j]:
      continue
    c[j] = True
    da += a[j]
    db += b[j]
    for k in g[j]:
      q.append(k)
  if da != db:
    ans = "No"
    break
print(ans)
