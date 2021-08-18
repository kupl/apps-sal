
N, M = list(map(int, input().split()))


grid = []
for _ in range(N):
    grid.append(list(input()))


def check(grid, i, j, sx, sy):
    if i - sx >= 0 and j - sy >= 0 and i + 2 - sx < N and j + 2 - sy < M:
        i -= sx
        j -= sy
        v = grid[i][j] == '#' and grid[i + 1][j] == '#' and grid[i + 2][j] == '#' and grid[i][j + 1] == '#' and grid[i + 2][j + 1] == '#' and grid[i][j + 2] == '#' and grid[i + 1][j + 2] == '#' and grid[i + 2][j + 2] == '#'
        return v

    return False


prev = False
for m in range(M):
    for n in range(N):
        if grid[n][m] == '#':
            if not (check(grid, n, m, 0, 0) or check(grid, n, m, 1, 0) or check(grid, n, m, 2, 0) or check(grid, n, m, 0, 1) or check(grid, n, m, 2, 1) or check(grid, n, m, 0, 2) or check(grid, n, m, 1, 2) or check(grid, n, m, 2, 2)):
                print("NO")
                return

print("YES")
