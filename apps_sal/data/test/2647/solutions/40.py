from collections import deque
H,W=map(int,input().split())
mp=[['#']*(W+2)]
count=0
for _ in range(H):
    l=list(input())
    mp.append(['#']+l+['#'])
    count+=l.count('.')
mp.append(['#']*(W+2))

dist=[[-1]*(W+2)for _ in range(H+2)]
Q=deque()
Q.append((1,1))
dist[1][1]=1
f=False

while Q:
    y,x=Q.popleft()
    if (y,x)==(H,W):
        f=True
        break
    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        ny=y+dy
        nx=x+dx
        if 0<=ny<H+2 and 0<=nx<W+2:
            if mp[ny][nx]=='.' and dist[ny][nx]==-1:
                Q.append((ny,nx))
                dist[ny][nx]=dist[y][x]+1

if f:
    print(count-dist[H][W])
else:
    print(-1)
