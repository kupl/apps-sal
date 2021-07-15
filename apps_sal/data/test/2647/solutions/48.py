import collections
import math


H,W=map(int,input().split())

c=[list(str(input())) for i in range(H)]
#1<=sy<=R
d=[[0 for j in range(W)]for i in range(H)]
inf=10**6
ans=0
for i in range(H):
    for j in range(W):
        if c[i][j]=='#':
            d[i][j]=-1
        else:
            d[i][j]=inf
            ans+=1


d[0][0]=0
queue=collections.deque([[0,0]])
gy,gx=H-1,W-1

moves=[[1,0],[-1,0],[0,1],[0,-1]]

flag=False
while len(queue)>0:
    now=queue.popleft()
    for i in range(4):
        ny=now[0]+moves[i][0]
        nx=now[1]+moves[i][1]
        
        if 0<=ny and ny<H and 0<=nx and nx<W and c[ny][nx]=='.' and d[ny][nx]==inf:
            d[ny][nx]=d[now[0]][now[1]]+1
            queue.append([ny,nx])
            if ny==gy and nx==gx:
                print(ans-d[ny][nx]-1)
                return
print(-1)     
