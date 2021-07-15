import sys
input=sys.stdin.readline
h,w,k=map(int,input().split())
si,sj,ti,tj=map(int,input().split())
si-=1
sj-=1
ti-=1
tj-=1
b=[input()for _ in range(h)]
ans=[[-1]*w for _ in range(h)]
ans[si][sj]=0
from collections import deque
d=deque()
d.append((si,sj))
while d:
  x,y=d.popleft()
  if x==ti and y==tj:
    print(ans[x][y]);return
  for dx,dy in [[1,0],[-1,0],[0,-1],[0,1]]:
    for i in range(1,k+1):
      xx=x+dx*i
      yy=y+dy*i
      if not(0<=xx<h and 0<=yy<w) or b[xx][yy]=="@":break
      if 0<=ans[xx][yy]<=ans[x][y]:break
      if ans[xx][yy]==-1:d.append((xx,yy))
      ans[xx][yy]=ans[x][y]+1
print(-1)

