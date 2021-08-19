

def fill(color_no, color_count, pos_x, pos_y, W, grid):

    while color_count > 0:
        grid[pos_y][pos_x] = color_no
        # print(pos_x,pos_y,grid)
        # 右端に到達
        if pos_x == W - 1 and pos_y % 2 == 0:
            pos_y = pos_y + 1
        # 左端に到達
        elif pos_x == 0 and pos_y % 2 == 1:
            pos_y = pos_y + 1
        # 右から左へ
        elif pos_y % 2 == 0:
            pos_x = pos_x + 1
        # 左から右へ
        elif pos_y % 2 == 1:
            pos_x = pos_x - 1
        color_count = color_count - 1

    return pos_x, pos_y, grid


H, W = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))

Grid = [[0] * W for i in range(H)]
pos_x = 0
pos_y = 0
for i in range(N):
    pos_x, pos_y, Grid = fill(i + 1, A[i], pos_x, pos_y, W, Grid)

for i in range(H):
    print((*Grid[i]))
