n,m=map(int,input().split())
xy=[[] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int,input().split())
    xy[x].append(y)
    xy[y].append(x)

from collections import deque

visited=[0]*(n+1)
count=0

for i in range(1,n+1):
    if visited[i]==0:
        stack=deque()
        stack.append(i)
        visited[i]+=1
        while stack:
            a=stack.pop()
            for j in xy[a]:
                if visited[j]==0:
                    visited[j]+=1
                    stack.append(j)
        count+=1
print(count)
