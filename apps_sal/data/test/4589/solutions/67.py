(H, W) = map(int, input().split())
x = [list(map(str, list(input()))) for l in range(H)]
for i in range(len(x)):
    x[i].insert(0, '.')
    x[i].append('.')
x.insert(0, ['.'] * (W + 2))
x.append(['.'] * (W + 2))
tmp = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if x[i][j] == '#':
            x[i][j] = '#'
            continue
        if x[i - 1][j - 1] == '#':
            tmp += 1
        if x[i - 1][j] == '#':
            tmp += 1
        if x[i - 1][j + 1] == '#':
            tmp += 1
        if x[i][j - 1] == '#':
            tmp += 1
        if x[i][j + 1] == '#':
            tmp += 1
        if x[i + 1][j - 1] == '#':
            tmp += 1
        if x[i + 1][j] == '#':
            tmp += 1
        if x[i + 1][j + 1] == '#':
            tmp += 1
        x[i][j] = str(tmp)
        tmp = 0
del x[0]
del x[-1]
for i in range(len(x)):
    del x[i][0]
    del x[i][-1]
for i in range(len(x)):
    print(''.join(x[i]))
