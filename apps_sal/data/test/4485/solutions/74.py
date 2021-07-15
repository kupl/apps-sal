from collections import deque

INF=10**20

N,M=map(int,input().split())
G=[[] for _ in range(N+1)]
for i in range(M):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)

def bfs(s):
    seen = [0 for i in range(N+1)]
    d = [0 for i in range(N+1)]
    todo = deque()
    seen[s]=1
    todo.append(s)
    while 1:
      if len(todo)==0:break
      a = todo.popleft()
      if d[a] >= 2:continue
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          d[b] += d[a] + 1
    return d

d = bfs(1)
if d[N] != 0 and d[N] <= 2:print('POSSIBLE')
else:print('IMPOSSIBLE')
