from heapq import heappop, heappush
N, M = list(map(int, input().split()))
#3 * i
edge = [[] for i in range(3 * N)]
for i in range(M):
  u, v = list(map(int, input().split()))
  u, v = u - 1, v - 1
  edge[3 * u].append(3 * v + 1)
  edge[3 * u + 1].append(3 * v + 2)
  edge[3 * u + 2].append(3 * v)
  
S, T = list(map(int, input().split()))  
S, T = S - 1, T - 1
#print(edge)

used = [0] * (3 * N)
queue = [[0, 3 * S]]
used[3 * S] = 1
while queue:
  time, now = heappop(queue)
  for i in edge[now]:
    if (i == 3 * T):
      print((int((time + 1) / 3)))
      return
    elif used[i] == 0:
      used[i] = 1
      heappush(queue, [time + 1, i])
    
    
print((-1))  
  
  
  




  

