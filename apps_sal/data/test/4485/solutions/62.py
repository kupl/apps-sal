n,m = map(int, input().split())

re = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  re[a].append(b)
  re[b].append(a)
  
reach = [0]*(n+1)
reach[1] = 1
for i in re[1]:
  if reach[i] == 0:
    for j in re[i]:
      reach[j] = 1

if reach[n] == 1:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")
