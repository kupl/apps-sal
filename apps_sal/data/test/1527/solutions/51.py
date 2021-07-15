from collections import deque
import numpy as np
H, W = map(int,input().split())
maze = [input() for _ in range(H)]

dxy =[[1,0],[0,1],[-1,0],[0,-1]]

ans = 0
for x in range(H):
    for y in range(W):
        if maze[x][y]=="#":
            continue
            
        seen = [[0]*W for _ in range(H)]
        que = deque([[x,y]])

        while que:
            vx,vy = que.popleft()
            for i,j in dxy:
                next_x,next_y = vx+i,vy+j
                if not(0<= next_x < H) or not(0<= next_y <W):
                    continue
                elif maze[next_x][next_y] !="#" and seen[next_x][next_y]==0:
                    seen[next_x][next_y]=seen[vx][vy]+1
                    que.append([next_x,next_y])
        seen[x][y] = 0
        ans = max(ans,np.max(seen))
print(ans)
