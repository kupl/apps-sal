h,w = map(int,input().split())
w_cnt = 0
L = []
for i in range(h):
    s = input()
    w_cnt += s.count(".")
    L.append(s)

from collections import deque
visited = [[0]*w for _ in range(h)]

q = deque([[0,0]])
li = [[1,0],[0,1],[-1,0],[0,-1]]

while q:
    y,x = q.popleft()
    for dy,dx in li:
        ny,nx = y+dy,x+dx
        if ny < 0 or ny >= h or nx < 0 or nx >= w or visited[ny][nx] > 0 or L[ny][nx] == "#" :
            continue
        visited[ny][nx] = visited[y][x] + 1
        if [ny,nx] == [h-1,w-1]:
            print(w_cnt-visited[ny][nx]-1)
            return
        q.append([ny,nx])
        
print(-1)
