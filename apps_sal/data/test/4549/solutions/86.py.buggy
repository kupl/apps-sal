h, w = list(map(int, input().split()))

square = []
for _ in range(h):
    square.append(input())


def check(i, j):
    flg = False
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if di + i < 0 or dj + j < 0:
            continue
        if di + i >= h or dj + j >= w:
            continue
        if square[di + i][dj + j] == "#":
            flg = True
    return flg


for i in range(h):
    for j in range(w):
        if square[i][j] == "#":
            if not check(i, j):
                # print(i,j)
                print('No')
                return

print('Yes')
