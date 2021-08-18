import itertools

dirs = (list(itertools.permutations(['r', 'l', 'd', 'u'])))

n, m = list(map(int, input().split()))
grid = []
for i in range(n):
    grid.append(input())

path = input()

dx = {
    'r': 0,
    'l': 0,
    'u': -1,
    'd': 1
}
dy = {
    'r': 1,
    'l': -1,
    'u': 0,
    'd': 0
}


def can_reach(n, m, grid, adir, path, dx, dy):
    x = y = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                x = i
                y = j
    for i in range(len(path)):
        x += dx[adir[int(path[i])]]
        y += dy[adir[int(path[i])]]
        if x >= n or y >= m or x < 0 or y < 0 or grid[x][y] == '
        return False
        if grid[x][y] == 'E':
            return True


cnt = 0
for adir in dirs:
    if can_reach(n, m, grid, adir, path, dx, dy):
        cnt += 1
print(cnt)
