h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

data = [[0] * w for i in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '
        data[i][j] = '
        else:
            for p in range(-1, 2):
                for q in range(-1, 2):
                    if 0 <= i + p < h and 0 <= j + q < w and s[i + p][j + q] == '
                    data[i][j] += 1
for i in range(h):
    print(*data[i], sep='')
