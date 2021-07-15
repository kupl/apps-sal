import sys
sys.setrecursionlimit(10**7)
from collections import deque

H,W=list(map(int,input().split()))
dots=H*W
field=[]
for _ in range(H):
    tmp=input()
    dots-=tmp.count("#")
    field.append(tmp)

DX=[1,0,-1,0]
DY=[0,1,0,-1]
dist=[[-1]*W for _ in range(H)]
dist[0][0]=0
que=deque()
que.append([0,0])

while que:
    y,x=que.popleft()
    for dx,dy in zip(DX,DY):
        nx=x+dx
        ny=y+dy
        if nx<0 or nx>=W or ny<0 or ny>=H: continue
        if field[ny][nx]=="#": continue
        if dist[ny][nx]==-1:
            dist[ny][nx]=dist[y][x]+1
            que.append([ny,nx])

score=-1
goal=dist[H-1][W-1]
if goal!=-1:
    score=dots-goal-1
print(score)

