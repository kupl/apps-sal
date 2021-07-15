from queue import Queue
S = list(map(int, input().strip()))
N = len(S)
graph = {}
for i in range(N):
 graph[S[i]] = []
if N > 1:
 for i in range(N):
  graph[S[i]].append(i)
 visited = [0] * N
 distance = [0] * N
 Q = Queue()
 Q.put(0)
 while (not Q.empty()):
  t = Q.get()
  for i in graph[S[t]]:
   if visited[i] == 0 and i != t:
    Q.put(i)
    visited[i] = 1
    distance[i] = distance[t] + 1
  graph[S[t]] = [] 
  if t > 0:
   if visited[t-1] == 0:
    Q.put(t-1)
    visited[t-1] = 1
    distance[t-1] = distance[t]+1
  if t < N-1:
   if visited[t+1] == 0:
    Q.put(t+1)
    visited[t+1] = 1
    distance[t+1] = distance[t]+1
  visited[t] = 1
 print(distance[-1])
else:
 print(0)
