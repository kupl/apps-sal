N = int(input())
XY = tuple((tuple(map(int, input().split())) for _ in range(N)))
lx = 0
rx = 1000
ans = 10 ** 18
for _ in range(100):
    ly = 0
    ry = 1000
    mlx = (2 * lx + rx) / 3
    for _ in range(100):
        mry = (ly + 2 * ry) / 3
        mly = (2 * ly + ry) / 3
        Rr = max(((x - mlx) ** 2 + (y - mry) ** 2 for (x, y) in XY))
        Rl = max(((x - mlx) ** 2 + (y - mly) ** 2 for (x, y) in XY))
        if Rl < Rr:
            ry = mry
        else:
            ly = mly
    R_left = Rl
    ly = 0
    ry = 1000
    mrx = (lx + 2 * rx) / 3
    for _ in range(100):
        mry = (ly + 2 * ry) / 3
        mly = (2 * ly + ry) / 3
        Rr = max(((x - mrx) ** 2 + (y - mry) ** 2 for (x, y) in XY))
        Rl = max(((x - mrx) ** 2 + (y - mly) ** 2 for (x, y) in XY))
        if Rl < Rr:
            ry = mry
        else:
            ly = mly
    R_right = Rl
    if R_left < R_right:
        rx = mrx
    else:
        lx = mlx
print(R_right ** 0.5)
