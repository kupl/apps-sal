(H, W) = list(map(int, input().split()))
S = ['.' * (W + 2)]
S += ['.' + input() + '.' for i in range(H)]
S += ['.' * (W + 2)]
ng = False
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if S[i][j] != '#':
            continue
        for (y, x) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if S[i + y][j + x] == '#':
                break
        else:
            ng = True
print('YNeos'[ng::2])
