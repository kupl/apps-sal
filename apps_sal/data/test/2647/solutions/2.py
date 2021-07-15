from collections import deque
import sys
h,w = map(int,input().split())
mp = [list(input()) for _ in range(h)]

visited = [[0]*w for _ in range(h)]

dxdy = [[1,0],[0,1],[-1,0],[0,-1]]

queue = deque()
queue.append([0,0,1])
visited[0][0]=1

while queue:
    x,y,d = queue.popleft()
    for dx,dy in dxdy:
        nx,ny = x+dx,y+dy
        if -1<nx<h and -1<ny<w and visited[nx][ny]==0 and mp[nx][ny]!="#":
            visited[nx][ny]=d+1
            queue.append([nx,ny,d+1])
            #[print(*visited[l]) for l in range(h)]
            #print("---------------")            

if visited[-1][-1]==0:
    print(-1)
    return

cnt = 0
for i in range(h):
    for j in range(w):
        if mp[i][j]!="#":
            cnt += 1

print(cnt-visited[-1][-1])
