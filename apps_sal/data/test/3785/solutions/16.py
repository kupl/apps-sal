import sys

def solve(n, m, k, grid, r, c):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for i in range(m)] for j in range(n)]
    q = [(r, c)]
    grid[r][c] = 'O'
    visited[r][c] = True
    k -= 1
    while k != 0 and len(q) != 0:
        r, c = q.pop()
        for i in range(4):
            x, y = r + move[i][0], c + move[i][1]
            if x >= 0 and x < n and y >= 0 and y < m and not visited[x][y] and grid[x][y] == '.':
                q.append((x, y))
                grid[x][y] = 'O'
                visited[x][y] = True
                k -= 1
                if k == 0:
                    break

n, m, k = list(map(int, sys.stdin.readline().split()))
grid = []
for i in range(n):
    s = list(input())
    grid.append(s)

r = 0
c = 0
cnt = 0
find = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            cnt += 1
            if not find:
                r, c = i, j
                find = True

solve(n, m, cnt-k, grid, r, c)

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            grid[i][j] = 'X'
#print(grid)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'O':
            grid[i][j] = '.'

for i in range(n):
    print(''.join(map(str, grid[i])))


