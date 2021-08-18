n = int(input())
grid = [list(input()) for _ in range(n)]

work = True
for i in range(n):
    for j in range(n):
        if grid[i][j] != '.':
            continue
        pos = [(i, j), (i + 1, j), (i + 2, j), (i + 1, j - 1), (i + 1, j + 1)]
        for r, c, in pos:
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] == '
            work = False
            break
            grid[r][c] = '
        else:
            continue
        break
    else:
        continue
    break
if work:
    print("YES")
else:
    print("NO")
