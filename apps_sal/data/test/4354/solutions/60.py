n, m = map(int, input().split())
sd = []
cp = []

for i in range(n):
  sd.append([int(j) for j in input().split()])
for i in range(m):
  cp.append([int(j) for j in input().split()])  
  
dist = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
  for j in range(m):
    dist[i][j] = abs(sd[i][0] - cp[j][0]) + abs(sd[i][1] - cp[j][1])
    
for i in range(n):
  print(dist[i].index(min(dist[i]))+1)
