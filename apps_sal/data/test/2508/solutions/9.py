#import heapq
from collections import deque
h,w,k = list(map(int, input().split()))
x1,y1,x2,y2 = list(map(int, input().split()))
x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
dp = [[-1]*w for _ in range(h)]
#que = []
que = deque()
c = [input() for _ in range(h)]

dp[x1][y1] = 0
#heapq.heappush(que, (dp[x1][y1], [x1,y1]))
que.append((x1,y1))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while que:
  #p= heapq.heappop(que)[1]
  #x,y= p[0],p[1]
  x,y = que.popleft()
  if (x == x2) & (y == y2):print(dp[x2][y2]);return
  for i in range(4):
    for j in range(1,k+1):
      nx = x + dx[i]*j
      ny = y + dy[i]*j
      if not ((0 <= nx < h) & (0 <= ny < w)):break
      if c[nx][ny] == '@':break
      if 0 <= dp[nx][ny] <= dp[x][y]:break
      if dp[nx][ny] == -1:
        #heapq.heappush(que, (dp[nx][ny], [nx,ny]))
        que.append((nx,ny))
      dp[nx][ny] = dp[x][y] + 1

print(-1)

