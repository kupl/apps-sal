N,M = map(int,input().split())
X = sorted([list(map(int,input().split())) for n in range(N)])
G = 0
D = 0

for m in range(M):
  if D+X[m][1]<M:
    D+=X[m][1]
    G+=X[m][0]*X[m][1]
  else:
    G+=X[m][0]*(M-D)
    print(G)
    return
