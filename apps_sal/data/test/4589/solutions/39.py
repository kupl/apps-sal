(h, w) = map(int, input().split())
l = [list(input()) for i in range(h)]
ans = [[0] * w for i in range(h)]
for i in range(h):
    for j in range(w):
        if l[i][j] == '#':
            ans[i][j] = '#'
        else:
            for p in range(-1, 2):
                for q in range(-1, 2):
                    if 0 <= i + p < h and 0 <= j + q < w and (l[i + p][j + q] == '#'):
                        ans[i][j] += 1
for i in range(h):
    print(*ans[i], sep='')
