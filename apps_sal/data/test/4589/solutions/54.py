h, w = map(int, input().split())
grid = [""] * h
for i in range(h):
    grid[i] = list(input())
search = [(row, col) for row in range(-1, 2) for col in range(-1, 2) if not(row == 0 and col == 0)]

for i in range(h):
    ans = ""
    for j in range(w):
        if(grid[i][j] == "."):
            bomb = 0
            for k in range(8):
                row, col = search[k]
                if(0 <= i + row < h and 0 <= j + col < w):
                    if(grid[i + row][j + col] == "
                        bomb += 1
            grid[i][j]=bomb
        ans += str(grid[i][j])
    print(ans)
