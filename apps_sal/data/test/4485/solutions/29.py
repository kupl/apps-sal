N,M = map(int,input().split())
#隣接リスト
g = [[] for i in range(N)]
for i in range(M):
  a,b = map(int,input().split())
  g[a-1].append(b)
  g[b-1].append(a)
ls = g[0]
flag = 0
for i in range(len(g[0])):
  ls2 = g[ls[i]-1]
  for j in range(len(ls2)):
    if ls2[j] == N:
      flag += 1
      print("POSSIBLE")
      break
if flag == 0:
  print("IMPOSSIBLE")
