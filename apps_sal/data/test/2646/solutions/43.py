from collections import deque

N,M = map(int,input().split())
room_g = [[] for i in range(N+1)]

for i in range(M):
  a,b = map(int,input().split())
  room_g[a].append(b)
  room_g[b].append(a)
  
sign = [-1]*(N+1)
sign[0] = 0
sign[1] = 0

d = deque()
d.append(1)

while d:
  x = d.popleft()
  for i in room_g[x]:
    if sign[i] != -1:
      continue
    sign[i] = x
    d.append(i)
    
ans = sign[2:]
print("Yes")
for i in range(len(ans)):
  print(ans[i])
