grid = [[-1] * 4 for i in range(4)]
for i in range(1, 4):
    grid[i][1], grid[i][2], grid[i][3] = list(map(int, input().split()))
    grid[i][0] = min(grid[i][1], grid[i][2], grid[i][3])
# print('----------')
# for i in range(4):
#    print(grid[i])

isOK = False
for i in range(grid[1][0] + 1):
    grid[0][0] = i
    grid[0][1] = grid[1][1] - i
    grid[0][2] = grid[1][2] - i
    grid[0][3] = grid[1][3] - i
#    print('----------')
#    for j in range(4):
#        print(grid[j])
    if grid[2][1] - grid[0][1] == grid[2][2] - grid[0][2] and grid[2][2] - grid[0][2] == grid[2][3] - grid[0][3]:
        if grid[3][1] - grid[0][1] == grid[3][2] - grid[0][2] and grid[3][2] - grid[0][2] == grid[3][3] - grid[0][3]:
            isOK = True
            break
if isOK:
    print('Yes')
else:
    print('No')
