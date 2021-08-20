(h, w) = map(int, input().split())
c = [list(input()) for i in range(h)]
ac = [[0] * w for i in range(2 * h)]
for i in range(2 * h):
    for j in range(w):
        ac[i][j] = c[i // 2][j]
for s in ac:
    print(*s, sep='')
