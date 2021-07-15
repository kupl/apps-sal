n,m = map(int,input().split())

l = [-1]*(n+1)

for _ in range(m):
  s,c = map(int,input().split())
  if l[s] == -1:
    l[s] = c
  else:
    if l[s] != c:
      print(-1)
      return

if n != 1 and l[1] == 0:
  print(-1)
  return
if l[1] == -1:
  l[1] = 1
for i in range(2,n+1):
  if l[i] == -1:
    l[i] = 0
ls = list(map(str,l))
if n == 1 and m == 0:
  print(0)
  return
print(int(''.join(ls[1:])))
