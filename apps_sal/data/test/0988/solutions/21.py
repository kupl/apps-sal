m = [[3, 3, 4, 4, 3, 3], [3, 3, 4, 4, 3, 3], [2, 2, 3, 3, 2, 2], [2, 2, 3, 3, 2, 2], [1, 1, 2, 2, 1, 1], [1, 1, 2, 2, 1, 1]]
mx = 0
k = [list(input().replace('-', '')) for i in range(6)]
for y in range(6):
    for x in range(6):
        if k[y][x] == '.':
            if m[y][x] > mx:
                mx = max(m[y][x], mx)
                maxpos = (y, x)
k[maxpos[0]][maxpos[1]] = 'P'
k = [l[:2] + ['-'] + l[2:4] + ['-'] + l[4:] for l in k]
for l in k:
    print(*l, sep='')
