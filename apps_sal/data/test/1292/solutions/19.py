import sys
import math
from collections import defaultdict, deque
import heapq
mod = 998244353


def check(x, y, n, m):
    return (0 <= x < n and 0 <= y < m)


n, m, k = list(map(int, sys.stdin.readline().split()))
grid = []
s = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    grid.append(list(sys.stdin.readline()[:-1]))
q = deque()
dic = defaultdict(deque)
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.' and grid[i][j] != '
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
            x, y, dis = nq.popleft()
            if dis == 0:
                dic[p].append([x, y])
            else:
                for i, j in dirs:
                    nx, ny = x + i, y + j
                    if check(nx, ny, n, m) and grid[nx][ny] == '.':
                        grid[nx][ny] = p
                        nq.append([nx, ny, dis - 1])

    if z:
        q = False

'''for i in range(k):
	for j in dic[i+1]:
		q.append([i+1]+j)

while q:
	p,curx,cury=q.popleft()

	nq=deque()
	nq.append([curx,cury,s[p-1]])
	if int(grid[curx][cury])==p:
		while nq:
			x,y,dis=nq.popleft()
			if dis==0:
				q.append([p,x,y])
			else:
				for i,j in dirs:
					nx,ny=x+i,y+j
					if check(nx,ny,n,m) and grid[nx][ny]=='.':
						grid[nx][ny]=p
						nq.append([nx,ny,dis-1])
	for i in range(n):
		print(grid[i])
	print('\n')'''
ans = [0 for _ in range(k)]
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.' and grid[i][j] != '
        ans[int(grid[i][j]) - 1] += 1
print(*ans)
