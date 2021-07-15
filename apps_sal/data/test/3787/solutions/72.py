n,a,b = map(int,input().split())
if not (a+b-1 <= n <= a*b):
  print(-1)
  return
n -= a
l = list()
for i in range(b,a*b+1,b):
  t = min(n,b-1)
  l += [i-j for j in range(t+1)]
  n -= t
d = dict()
g = sorted(l)
for i,x in enumerate(g,1):
  d[x] = i
l = list(map(lambda x:d[x], l))
print(*l)
