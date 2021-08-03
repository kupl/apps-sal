A, B = map(int, input().split())
Grid = []
for i in range(100):
    Grid += [[0] * 100]
acgrid = []
for _ in range(50):
    acgrid.append(1)
    acgrid.append(-1)
white = 1
black = 1
if A == 1 and B == 0:
    Grid = [1, -1]
else:
    i = 0
    while True:
        if white + 50 > A:
            break
        else:
            Grid[i] = acgrid
            Grid[i + 1] = [-1] * 100
            i += 2
            white += 50
    for j in range(50):
        if white != A:
            Grid[i][2 * j] = 1
            Grid[i][2 * j + 1] = -1
            white += 1
        else:
            Grid[i][2 * j] = -1
            Grid[i][2 * j + 1] = -1
    i += 1
    Grid[i] = [-1] * 100
    i += 1
    Grid[i] = [1] * 100
    i += 1
    while True:
        if black + 50 > B:
            break
        else:
            Grid[i] = acgrid
            Grid[i + 1] = [1] * 100
            i += 2
            black += 50
    for j in range(50):
        if black != B:
            Grid[i][2 * j] = 1
            Grid[i][2 * j + 1] = -1
            black += 1
        else:
            Grid[i][2 * j] = 1
            Grid[i][2 * j + 1] = 1
num = []
ans = []
for box in Grid:
    if box[0] == 0:
        break
    else:
        st = ''
        for s in box:
            if s == 1:
                st += '.'
            elif s == -1:
                st += '#'
        ans.append(st)
num.append(len(ans))
num.append(len(ans[0]))
print(num[0], num[1])
for st in ans:
    print(st)
