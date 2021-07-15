import sys
#sys.stdin=open('in.txt')
sys.setrecursionlimit(10000)
isin = lambda x, y: 0<=x<m and 0<=y<n

def dfs(curx, cury, fax=-1, fay=-1):
    nonlocal found
    vis[curx][cury]=True
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0, 0]
    for i in range(4):
        newx=curx+dx[i]
        newy=cury+dy[i]
        if isin(newx,newy) and vis[newx][newy] and G[curx][cury]==G[newx][newy] and not (fax == newx and fay == newy):
            found=True
        if isin(newx,newy) and not vis[newx][newy] and G[curx][cury]==G[newx][newy]:
            dfs(newx, newy, curx, cury)   

m,n = list(map(int, input().split()))
vis=[[False]*n for i in range(m)]
found=False
G=[input() for i in range(m)]
for i in range(m):
    for j in range(n):
        found = False
        if not vis[i][j]:
            dfs(i, j)
        if found:
            print('Yes')
            return
print('No')    

