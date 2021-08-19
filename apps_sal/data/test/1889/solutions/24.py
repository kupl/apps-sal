(rows, cols, changes_count) = list(map(int, input().split()))
grid = [input().split() for _ in range(rows)]
changes = [list(map(int, input().split())) for __ in range(changes_count)]
max_line = [max(list(map(len, ''.join(row).split('0')))) for row in grid]
for (r, c) in changes:
    grid[r - 1][c - 1] = '0' if grid[r - 1][c - 1] == '1' else '1'
    max_line[r - 1] = max(list(map(len, ''.join(grid[r - 1]).split('0'))))
    print(max(max_line))
