import sys
from collections import deque

input=sys.stdin.readline


n,m=list(map(int,input().split()))
w=list(map(int,input().split()))
data=[[] for i in range(n)]
fav=[]
for i in range(m):
    x,y=list(map(int,input().split()))
    x,y=min(x,y),max(x,y)
    w[x-1]-=1
    w[y-1]-=1
    data[x-1].append(i)
    data[y-1].append(i)
    fav.append((x-1,y-1))

ans=[]
used=[False]*m
useddish=[False]*n

que=deque([])
for i in range(n):
    if w[i]>=0:
        que.append(i)
        useddish[i]=True

while que:
    id=que.popleft()
    for i in data[id]:
        if not used[i]:
            used[i]=True
            ans.append(i)
            x,y=fav[i]
            w[x]+=1
            w[y]+=1
            if w[x]>=0 and not useddish[x]:
                que.append(x)
                useddish[x]=True
            if w[y]>=0 and not useddish[y]:
                que.append(y)
                useddish[y]=True

if len(ans)==m:
    print("ALIVE")
    ans=[ans[-i-1]+1 for i in range(m)]
    print(*ans)
else:
    print("DEAD")

