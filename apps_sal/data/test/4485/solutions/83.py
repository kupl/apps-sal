n,m = list(map(int,input().split()))
e = [list() for _ in range(n)]
for i in range(m):
    a,b = list(map(int,input().split()))
    e[a-1].append(b-1)
    e[b-1].append(a-1)

visited = [float("inf")]*n
visited[0]=0
from collections import deque
queue = deque()
queue.append([0,0])

while queue:
    v,d = queue.popleft()
    for k in e[v]:
        if visited[k]==float("inf"):
            visited[k]=d+1
            queue.append([k,d+1])
            #print(visited)
if visited[n-1]<=2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")


