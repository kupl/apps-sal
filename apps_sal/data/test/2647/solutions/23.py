import sys
from collections import deque
input = sys.stdin.readline

H,W = map(int,input().split())
sy, sx = 0,0
gy, gx = H-1,W-1
D = [list(input()) for i in range(H)]
Bs = 0
for i in range(H):
    Bs += D[i].count("#")

Q = deque()
Q.append((sy,sx))
dist = [[-1]*W for i in range(H)]
dist[sy][sx] = 0
dx = [1,0,-1,0]
dy = [0,-1,0,1]

while Q:
    x,y = Q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<=W-1 and 0<=ny<=H-1 and D[ny][nx]!="#" and dist[ny][nx] == -1:
            Q.append((nx,ny))
            dist[ny][nx] = dist[y][x]+1

print(H*W-Bs-1-dist[gy][gx] if dist[gy][gx]!=-1 else -1)
