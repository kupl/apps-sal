N,M = map(int, input().split())

G = [[] for _ in range(N)]
INF = 10**9
D = [[ INF for _ in range(N)] for _ in range(N)]
for i in range(N):
  D[i][i] = 0

E = []
for _ in range(M):
  a,b,c = map(int, input().split())
  a,b = a-1, b-1
  G[a].append((b,c))
  G[b].append((a,c))
  D[a][b] = c
  D[b][a] = c
  E.append((a,b,c))
  

for k in range(N):
  for i in range(N):
    for j in range(N):
      if D[i][k] + D[k][j] < D[i][j]:
        D[i][j] = D[i][k] + D[k][j]
        D[j][i] = D[i][k] + D[k][j]
  
ans = 0
for a,b,c in E:
  flg = False
  for i in range(N):
    if D[i][a] + c == D[i][b]:
      flg = True
      break
   
  if not flg:
    ans += 1
    
print(ans)
