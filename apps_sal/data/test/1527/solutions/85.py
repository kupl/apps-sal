H,W=map(int,input().split())
S=[list(input())for _ in range(H)]

from collections import deque
import math


def bfs(h,w,sy,sx,S):
    maze=[[10**9]*(W)for _ in range(H)]

    maze[sy-1][sx-1]=0
    que=deque([[sy-1,sx-1]])
    count=0
    while que:
        y,x=que.popleft()
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            nexty,nextx=y+i,x+j
            if 0<=nexty<h and 0<=nextx<w:
                dist1=S[nexty][nextx]
                dist2=maze[nexty][nextx]
            else:
                continue
            if dist1!='#':
                if dist2>maze[y][x]+1:
                    maze[nexty][nextx]=maze[y][x]+1
                    count=max(count,maze[nexty][nextx])
                    que.append([nexty,nextx])
    return count

ans=0
for sy in range(H):
    for sx in range(W):
        if S[sy][sx]=='.':
            now=bfs(H,W,sy+1,sx+1,S)
            ans=max(ans,now)

print(ans)
