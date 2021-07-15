from scipy.sparse.csgraph import floyd_warshall
N,M,L,*X = map(int, open(0).read().split())
ls = X[:3*M]
Els = [[0]*N for i in range(N)]
Q = X[3*M]
query = X[3*M+1:]
for a,b,c in zip(*[iter(ls)]*3):
  if c<=L:
    Els[a-1][b-1] = c
    Els[b-1][a-1] = c
dist = floyd_warshall(Els)
      
Els2 = [[0]*N for i in range(N)]
for i in range(N):
  for j in range(N):
    if dist[i][j]<=L:
      Els2[i][j] = 1
ans = floyd_warshall(Els2)

for s,t in zip(*[iter(query)]*2):
  if ans[s-1][t-1]==float('inf'):
    print(-1)
    continue
  print(int(ans[s-1][t-1])-1)
