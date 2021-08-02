import sys
import math
from collections import defaultdict, deque
import heapq
n, m = list(map(int, sys.stdin.readline().split()))
grid = []
for i in range(n):
    s = sys.stdin.readline()[:-1]
    grid.append(s)
right = [[0 for _ in range(m)] for x in range(n)]
for i in range(n):
    l, r, cnt = 0, 0, 0
    while r < m:
        cnt = 0
        while r < m and grid[i][l] == grid[i][r]:
            cnt += 1
            r += 1
        while l < r:
            right[i][l] = cnt
            cnt -= 1
            l += 1
'''for i in range(n):
	print(right[i])'''
down = [[0 for _ in range(m)] for x in range(n)]
for i in range(m):
    l, r, cnt = 0, 0, 0
    while r < n:
        cnt = 0
        while r < n and grid[l][i] == grid[r][i]:
            cnt += 1
            r += 1
        while l < r:
            down[l][i] = cnt
            cnt -= 1
            l += 1
'''for i in range(n):
	print(down[i],'down')'''
ans = 0
for i in range(n):
    for j in range(m):
        x = down[i][j]
        y = 0
        if i + x < n:
            y = down[i + x][j]
        z = 0
        if i + x + y < n:
            z = down[i + x + y][j]
        if x == y and z >= y:
            # print(x,'x',y,'y',z,'z',i,'i',j,'j')
            minn = right[i][j]
            for k in range(i, i + 3 * x):
                minn = min(minn, right[k][j])
            # print(minn,'minn')
            # print(i,'i',j,'j')
            ans += minn
print(ans)
