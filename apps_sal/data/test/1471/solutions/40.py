n = int(input())
d = [[] for i in range(n)]
for i in range(n-1):
  u, v, w = map(int, input().split())
  d[u-1].append([v-1, w])
  d[v-1].append([u-1, w])
  
ans = [[] for i in range(n)]
ans[0].append(0)
q = [0]

while q:
  x = q.pop()
  for u, w in d[x]:
    if not ans[u]:
      buf = ans[x][0]
      if w%2==1:
        buf = (buf+1)%2
      ans[u].append(buf)
      q.append(u)
    
for i in ans:
  print(*i)
