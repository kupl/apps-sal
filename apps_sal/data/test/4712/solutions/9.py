h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

d = [['#'] * (w + 2) for i in range(h + 2)]
for i in range(h):
    for j in range(w):
        d[i + 1][j + 1] = a[i][j]
for i in range(h + 2):
    print(*d[i], sep='')
