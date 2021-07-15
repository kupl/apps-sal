n,m=map(int,input().split())
a=[list(input()) for _ in range(n)]
b=[list(input()) for _ in range(m)]

eq = False
find = False
for i in range(n-m+1):
  for j in range(n-m+1):
    for p in range(m):
      for q in range(m):
        if a[p+i][q+j] == b[p][q]:
          eq = True
        else:
          eq = False
          break
      if not eq:
        break
    if eq:
      find = True
      break
  if find:
    break
if find:
  print('Yes')
else:
  print('No')
