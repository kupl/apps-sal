h, w = list(map(int, input().split()))
grid = (h + 1) * [None]
grid[0] = (w + 1) * '#'
for r in range(1, h + 1):
    grid[r] = '#' + input().strip()

rt = [[0 for c in range(w + 1)] for r in range(h + 1)]
for r in range(1, h + 1):
    for c in range(1, w + 1):
        if '.' == grid[r][c] == grid[r][c - 1]:
            delta = 1
        else:
            delta = 0
        rt[r][c] = rt[r][c - 1] + delta
    for c in range(1, w + 1):
        rt[r][c] += rt[r - 1][c]
ct = [[0 for c in range(w + 1)] for r in range(h + 1)]
for c in range(1, w + 1):
    for r in range(1, h + 1):
        if '.' == grid[r][c] == grid[r - 1][c]:
            delta = 1
        else:
            delta = 0
        ct[r][c] = ct[r - 1][c] + delta
    for r in range(1, h + 1):
        ct[r][c] += ct[r][c - 1]

debug = False
if debug:
    print()
    for r in range(1, h + 1):
        print(grid[r][1:])
        print(rt[r][1:])
    print()
    for c in range(1, w + 1):
        print(''.join([grid[r][c] for r in range(1, h + 1)]))
        print([ct[r][c] for r in range(1, h + 1)])
    print()

q = int(input())
for i in range(q):
    r, c, R, C = list(map(int, input().split()))
    if debug:
        print((rt[R][C], -rt[R][c], -rt[r - 1][C], rt[r - 1][c], '\n',
              ct[R][C], -ct[r][C], -ct[R][c - 1], ct[r][c - 1]))
    x = rt[R][C] - rt[R][c] - rt[r - 1][C] + rt[r - 1][c] + \
        ct[R][C] - ct[r][C] - ct[R][c - 1] + ct[r][c - 1]
    print(x)
