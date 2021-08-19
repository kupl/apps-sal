(h, w) = map(int, input().split())
l = []
for i in range(h):
    s = list(input().replace('.', '0'))
    l.append(s)
for i in range(h):
    for j in range(w):
        if l[i][j] == '#':
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x <= h - 1 and 0 <= y <= w - 1:
                        if l[x][y] != '#':
                            l[x][y] = str(int(l[x][y]) + 1)
for i in range(h):
    print(''.join(l[i]))
