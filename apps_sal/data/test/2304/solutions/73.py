from collections import deque
N,M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  l,r,d = map(int, input().split())
  l,r = l-1,r-1
  E[l].append((r,d))
  E[r].append((l,-d)) 
  
#for e in E:
#  print(e)
  
# bfs
Q = deque()
visited = [False] * N
willSearch = [False] * N
INF = 10**16
A = [ INF ] * N

for i in range(N):
  if visited[i]:
    continue
  Q.append((i,-1,0))
  while Q:
    now, prev, num = Q.popleft()
    visited[now] = True
    if A[now] == INF:
      A[now] = num
    elif A[now] != num:
      # ある点において2通りのnum設定の仕方がある
      #print(now,prev,num,A[inxt])
      print("No")
      return
    for nxt, dis in E[now]:
      if nxt == prev:
        continue
      if A[nxt] < INF and A[nxt] != num + dis:
        # ある点において2通りのnum設定の仕方がある
        #print(now,prev,num, nxt,dis, A[nxt])
        print("No")
        return
      if visited[nxt] or willSearch[nxt]:
        continue
      Q.append((nxt, now, num + dis))
      willSearch[nxt] = True
    
print("Yes")
