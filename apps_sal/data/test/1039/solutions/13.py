n=int(input())
abc=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    abc[a].append([b,c])
    abc[b].append([a,c])
from collections import deque
q,k=map(int,input().split())
visited=[0]*(n+1)
distance=[0]*(n+1)
que=deque()
que.append(k)
visited[k]+=1
count=0
while que:
    x=que.pop()
    for y in abc[x]:
        if visited[y[0]]==0:
            distance[y[0]]+=distance[x]+y[1]
            visited[y[0]]+=1
            que.appendleft(y[0])
for j in range(q):
    c,d=map(int,input().split())
    print(distance[c]+distance[d])
