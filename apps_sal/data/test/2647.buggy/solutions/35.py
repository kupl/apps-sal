(H, W) = list(map(int, input().split()))
grid = [input() for _ in range(H)]
checked = [[False] * W for _ in range(H)]


def solve(arr, count):
    next_arr = set()
    count += 1
    for a in arr:
        (y, x) = (a[0], a[1])
        checked[y][x] = True
        if y == H - 1 and x == W - 1:
            return count
        if y < H - 1:
            if not checked[y + 1][x] and grid[y + 1][x] == '.':
                next_arr.add((y + 1, x))
        if 0 < y:
            if not checked[y - 1][x] and grid[y - 1][x] == '.':
                next_arr.add((y - 1, x))
        if x < W - 1:
            if not checked[y][x + 1] and grid[y][x + 1] == '.':
                next_arr.add((y, x + 1))
        if 0 < x:
            if not checked[y][x - 1] and grid[y][x - 1] == '.':
                next_arr.add((y, x - 1))
    if len(next_arr) == 0:
        return -1
    return solve(next_arr, count)


min_steps = solve([(0, 0)], 0)
if min_steps == -1:
    print(-1)
else:
    w_c = 0
    for i in grid:
        w_c += i.count('.')
    print(w_c - min_steps)
