n,m = map(int, input().split())
t = [[n] for i in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  t[a-1].append(b-1)
g = []
for i in t:
  g.append(min(i))
k = 0
ans=0
while k <=n-1:
  e = min(g[k:])
  if e==n:
    break
  ans+=1
  k = e
print(ans)
