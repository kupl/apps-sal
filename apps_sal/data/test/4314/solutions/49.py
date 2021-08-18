h, w = list(map(int, input().split()))
grid = [input() for _ in range(h)]


def check_row(grid):
    for i in range(len(grid)):
        if "
        return i
    return -1


def check_col(grid):
    grid_inv = []
    for i in range(len(grid[0])):
        grid_inv.append("".join(row[i] for row in grid))
    return check_row(grid_inv)


while True:
    if check_row(grid) != -1:
        del grid[check_row(grid)]
        continue
    elif check_col(grid) != -1:
        d = check_col(grid)
        for i in range(len(grid)):
            grid[i] = grid[i][:d] + grid[i][d + 1:]
    else:
        break

for g in grid:
    print(g)
