from collections import deque

def put():
    return list(map(int, input().split()))
def safe(i,j):
    return i>=0 and j>=0 and i<n and j<m and vis[i][j]==0 and mat[i][j]=='.'

n,m = put()
sx,sy = put()
l,r = put()
sx,sy = sx-1,sy-1
mat = [input() for _ in range(n)]

vis = [[0]*m for _ in range(n)]
q = deque()
move = [(-1,0), (1,0), (0,-1), (0,1)]
ans  = 0

if safe(sx,sy):
    vis[sx][sy]=1
    q.append((sx,sy,0))
while q:
    x,y,s = q.popleft()
    R = s+(y-sy)
    L = s-(y-sy)
    if R<=2*r and L<=2*l:
        ans+=1

    for dx,dy in move:
        i,j = x+dx, y+dy
        if safe(i, j):
            vis[i][j]=1
            if dx==0:
                q.append((i,j,s+1))
            else:
                q.appendleft((i,j,s))
            

print(ans)

