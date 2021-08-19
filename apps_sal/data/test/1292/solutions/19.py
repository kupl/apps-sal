import sys
import math
from collections import defaultdict, deque
import heapq
mod = 998244353


def check(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


(n, m, k) = list(map(int, sys.stdin.readline().split()))
grid = []
s = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    grid.append(list(sys.stdin.readline()[:-1]))
q = deque()
dic = defaultdict(deque)
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.' and grid[i][j] != '#':
            dic[int(grid[i][j])].append([i, j])
q = True
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while q:
    z = True
    for i in range(k):
        nq = deque()
        while dic[i + 1]:
            j = dic[i + 1].popleft()
            nq.append(j + [s[i]])
            z = False
        p = i + 1
        while nq:
            (x, y, dis) = nq.popleft()
            if dis == 0:
                dic[p].append([x, y])
            else:
                for (i, j) in dirs:
                    (nx, ny) = (x + i, y + j)
                    if check(nx, ny, n, m) and grid[nx][ny] == '.':
                        grid[nx][ny] = p
                        nq.append([nx, ny, dis - 1])
    if z:
        q = False
"for i in range(k):\n\tfor j in dic[i+1]:\n\t\tq.append([i+1]+j)\n#print(q,'q')\n\nwhile q:\n\tp,curx,cury=q.popleft()\n\n\t#print(p,'p',curx,'curx',cury,'cury',s[p-1])\n\tnq=deque()\n\tnq.append([curx,cury,s[p-1]])\n\tif int(grid[curx][cury])==p:\n\t\twhile nq:\n\t\t\tx,y,dis=nq.popleft()\n\t\t\t#print(x,'x',y,'y',dis,'dis')\n\t\t\tif dis==0:\n\t\t\t\tq.append([p,x,y])\n\t\t\telse:\n\t\t\t\tfor i,j in dirs:\n\t\t\t\t\tnx,ny=x+i,y+j\n\t\t\t\t\tif check(nx,ny,n,m) and grid[nx][ny]=='.':\n\t\t\t\t\t\tgrid[nx][ny]=p\n\t\t\t\t\t\t#print(nx,'nx',ny,'ny',dis-1,'dis-1')\n\t\t\t\t\t\tnq.append([nx,ny,dis-1])\n\tfor i in range(n):\n\t\tprint(grid[i])\n\tprint('\n')"
ans = [0 for _ in range(k)]
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.' and grid[i][j] != '#':
            ans[int(grid[i][j]) - 1] += 1
print(*ans)
