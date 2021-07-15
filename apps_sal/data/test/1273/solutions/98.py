n = int(input())
A = []
g  =[[] for _ in range(n+1)]
ans = {}
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    A.append([a,b])
 
 
from collections import deque
 
q = deque()
q.append(1)
 
color = [-1]*(n+1)
color[1] = 0
cnt = 0
 
while q:
    v = q.popleft()
    p = 1
    for u in g[v]:
        if p==color[v]:
            p += 1
        color[u] = p
        ans[v,u] = p
        q.append(u)
        cnt = max(cnt,p)
        p += 1
print(cnt)
 
for i in range(n-1):
    tmp = (A[i][0],A[i][1])
    print(ans[tmp])
