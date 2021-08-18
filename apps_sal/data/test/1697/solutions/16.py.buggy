import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input().rstrip())

visited = [[False for _ in range(m)] for _ in range(n)]
foundCycle = False

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, fromX, fromY, color):
    nonlocal board, visited, foundCycle

    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if board[x][y] != color:
        return

    if visited[x][y]:
        foundCycle = True
        return

    visited[x][y] = True
    for f in range(4):
        nextX = x + dx[f]
        nextY = y + dy[f]
        if nextX == fromX and nextY == fromY:
            continue
        dfs(nextX, nextY, x, y, color)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, -1, -1, board[i][j])
print("Yes" if foundCycle else "No")
