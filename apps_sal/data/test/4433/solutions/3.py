import collections
n,m = [int(x) for x in input().split()]

G = []
for _ in range(n):
    G.append([])
    
for _ in range(m):
    a,b = [int(x)-1 for x in input().split()]
    G[a].append((a,b))
    G[b].append((b,a))

best,index = 0,0
for i in range(n):
    if len(G[i]) > best:
        best = len(G[i])
        index = i
    
    
visited, edges = [0]*n, []
visited[index] = 1
queue = collections.deque(G[index])
while queue:
    vertex = queue.popleft()
    if visited[vertex[1]] == 0:
        visited[vertex[1]] = 1
        edges.append((vertex))
        queue.extend(G[vertex[1]])

for e in edges:
    print(e[0]+1,e[1]+1)
