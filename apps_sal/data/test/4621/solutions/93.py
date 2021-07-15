H, W = map(int,input().split())
grid = []
for i in range(H):
    array = list(input().strip().split())
    grid.append(array)

for i in range(H):
    print(''.join(grid[i]))
    print(''.join(grid[i]))
