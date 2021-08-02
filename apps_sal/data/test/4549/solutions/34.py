H, W = map(int, input().split())
grid = []
ans = "Yes"

for _ in range(H):
    grid_i = input().split()
    grid.append(grid_i[0])

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            X = "NG"
            if (i - 1 >= 0 and grid[i - 1][j] == ".") or i < 1:
                None
            else:
                X = "OK"
            if (j - 1 >= 0 and grid[i][j - 1] == ".") or j < 1:
                None
            else:
                X = "OK"
            if (i + 1 < H and grid[i + 1][j] == ".") or i + 1 >= H:
                None
            else:
                X = "OK"
            if (j + 1 < W and grid[i][j + 1] == ".") or j + 1 >= W:
                None
            else:
                X = "OK"
            if X == "NG":
                ans = "No"

print(ans)
