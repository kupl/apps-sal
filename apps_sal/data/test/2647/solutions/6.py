from collections import deque

h,w=map(int,input().split())
w_sum=0
maze=[]
inf=10000000
for _ in range(h):
  s=list(input())
  for i in range(w):
    if s[i]=='.':
      s[i]=inf
      w_sum+=1
  maze.append(s)
  
def solve(maze,h,w):
  qu=deque([[0,0]])
  maze[0][0]=0
  while qu:
    y,x=qu.popleft()
    t=maze[y][x]
    for i in ([1,0],[-1,0],[0,1],[0,-1]):
      ny=y+i[0]
      nx=x+i[1]
      if 0<=ny<=h-1 and 0<=nx<=w-1 and maze[ny][nx]!='#':
        if maze[ny][nx]>t+1:
          maze[ny][nx]=t+1
          qu.append([ny,nx])
          
  return maze[h-1][w-1]
  
if solve(maze,h,w)==inf:
  print(-1)
else:
  print(w_sum-solve(maze,h,w)-1)
