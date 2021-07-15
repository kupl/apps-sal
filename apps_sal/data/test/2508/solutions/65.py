from collections import deque
h, w, k = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
c = []
for _ in range(h):
    c.append(input())
q = deque([(x1-1, y1-1)])
dxdy = [(-1,0), (0,-1), (0,1), (1,0)]
dist = [[1000000]*w for _ in range(h)]
dist[y1-1][x1-1] = 0
while q:
    x, y = q.popleft()
    for ddx, ddy in dxdy:
        for i in range(1, k+1):
            dx = ddx*i
            dy = ddy*i
            if not (0<=x+dx<w and 0<=y+dy<h):
                break
            if c[y+dy][x+dx]=='@' or dist[y+dy][x+dx]<=dist[y][x]:
                break
            if x+dx==x2-1 and y+dy==y2-1:
                print(dist[y][x]+1)
                return
            if dist[y+dy][x+dx]>dist[y][x]+1:
                dist[y+dy][x+dx] = dist[y][x]+1
                q.append((x+dx, y+dy))
print(-1)
