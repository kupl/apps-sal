from collections import deque
n = int(input())
m = []
for i in range(n):
  a = [*map(int,input().split())]
  m.append(a)
d = [0]*n
c = [0]*n
q = deque(range(n))
while q:
  p = q.popleft()
  if c[p-1]<n-1:
    e = m[p-1][c[p-1]]
    if p==m[e-1][c[e-1]]:
      t=max(d[p-1],d[e-1])+1
      d[p-1]=t
      d[e-1]=t
      c[p-1]+=1
      c[e-1]+=1
      q.append(p)
      q.append(e)
if min(c)!=n-1:
  print(-1)
else:
  print(max(d))
