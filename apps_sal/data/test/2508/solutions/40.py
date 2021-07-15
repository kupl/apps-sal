from collections import deque
h,w,k = map(int,input().split())
a,b,c,d = map(int,input().split())
a -= 1
b -= 1
c -= 1
d -= 1
maze = [input() for _ in range(h)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
depth = [[float("inf") for _ in range(w)] for _ in range(h)]
dq = deque([(b,a)])
depth[a][b] = 0
while dq:
    x,y = dq.popleft()
    if x == d and y == c:
        break
    for i in range(4):
        nx,ny,K = x,y,k
        while K:
            K -= 1
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<=w-1 and 0<=ny<=h-1 and maze[ny][nx] != "@" and depth[ny][nx] > depth[y][x]:
                if depth[ny][nx] == depth[y][x]+1:
                    continue
                depth[ny][nx] = depth[y][x] +1
                dq.append((nx,ny))
            else:
                break
print(depth[c][d] if depth[c][d] != float("inf") else -1)
