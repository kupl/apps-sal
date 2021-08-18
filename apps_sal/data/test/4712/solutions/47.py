h, w = map(int, input().split())
grid = [["

for i in range(h):
    grid[i + 1] = ["

for i in range(h + 2):
    print("".join(grid[i]))
