(h, w) = list(map(int, input().split()))
grid = [[-1 for i in range(w)] for j in range(h)]
isValid = True
rs = list(map(int, input().split()))
for y in range(h):
    for j in range(rs[y]):
        grid[y][j] = 1
    if rs[y] != w:
        grid[y][rs[y]] = 0
cs = list(map(int, input().split()))
for x in range(w):
    for j in range(cs[x]):
        if grid[j][x] == 0:
            isValid = False
        grid[j][x] = 1
    if cs[x] != h:
        if grid[cs[x]][x] == 1:
            isValid = False
        grid[cs[x]][x] = 0
total = 1
for i in range(h):
    for j in range(w):
        if grid[i][j] == -1:
            total *= 2
            total %= 1000000007
if isValid:
    print(total)
else:
    print(0)
