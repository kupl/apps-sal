n, k = map(int, input().split())
grid = []
gridx = set()
gridy = set()
for i in range(n):
    x, y = map(int, input().split())
    grid.append((x, y))
    gridx.add(x)
    gridy.add(y)
gridxl = sorted(gridx)
xlen = len(gridxl)
gridyl = sorted(gridy)
ylen = len(gridyl)
atable = [[0 for _ in range(ylen + 1)] for _ in range(xlen + 1)]
for i in range(n):
    (px, py) = grid[i]
    xid = gridxl.index(px)
    yid = gridyl.index(py)
    atable[yid + 1][xid + 1] = 1
for i in range(1, ylen + 1):
    for j in range(1, xlen + 1):
        atable[i][j] += atable[i][j - 1]
for j in range(1, xlen + 1):
    for i in range(1, ylen + 1):
        atable[i][j] += atable[i - 1][j]
gmin = 99999999999999999999
for x1 in range(1, xlen):
    for x2 in range(x1, xlen + 1):
        for y1 in range(1, ylen):
            for y2 in range(y1, ylen + 1):
                a = atable[y2][x2]
                b = atable[y1 - 1][x2]
                c = atable[y2][x1 - 1]
                d = atable[y1 - 1][x1 - 1]
                rui = a - b - c + d
                if rui >= k:
                    r = (gridxl[x2 - 1] - gridxl[x1 - 1]) * (gridyl[y2 - 1] - gridyl[y1 - 1])
                    if gmin > r:
                        gmin = min(gmin, r)
print(gmin)
