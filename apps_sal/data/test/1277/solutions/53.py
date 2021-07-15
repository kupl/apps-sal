from collections import deque
N,U,V = map(int, input().split())
U,V = U-1, V-1
E = [[] for _ in range(N)]

for _ in range(N-1):
  a,b = map(int, input().split())
  a,b = a-1, b-1
  E[a].append(b)
  E[b].append(a)

def BFS(root):
  D = [ 0 for _ in range(N) ]
  visited = [False for _ in range(N)]
  willSearch = [ False for _ in range(N)]
  Q = deque()
  Q.append(root)
  willSearch[root] = True
  while len(Q) > 0:
    now = Q.pop()
    visited[now] = True
    for nx in E[now]:
      if visited[nx] or willSearch[nx]:
        continue
      willSearch[nx] = True
      D[nx] = D[now] + 1
      Q.append(nx)
  return D

UD = BFS(U)
VD = BFS(V)

#print(UD)
#print(VD)

#初手で青木くんのPOINTにしか行けないケース
if E[U] == [V]:
  print(0)
  return
  
ans=0
 
for i in range(N):
    if UD[i]<=VD[i]:
        ans=max(ans,VD[i]-1)

print(ans)
