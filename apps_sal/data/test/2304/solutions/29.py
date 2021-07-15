from heapq import heappop, heappush
N, M = list(map(int, input().split()))
graph = [[] for i in range(N)]
root = [-float("inf")] * N
for i in range(M):
  l, r, d = list(map(int, input().split()))
  graph[l - 1].append([r - 1, d])
  graph[r - 1].append([l - 1, -d])
  
  
for i in range(N):
  if root[i] < -10 ** 10:
    root[i] = 0
    queue = [i]
    while queue:
      now = heappop(queue)
      for j, k in graph[now]:
        if root[j] < - 10 ** 10:
          root[j] = root[now] + k
          heappush(queue, j)
        elif root[j] == root[now] + k:
          continue
        else:
          print("No")
          return
          
print("Yes")


    
    
    
    
    

