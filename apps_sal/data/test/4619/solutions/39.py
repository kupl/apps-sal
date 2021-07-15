whn = list(map(int, input().split()))
w, h, n = whn[0], whn[1], whn[2]
xyas = [list(map(int, input().split())) for _ in range(n)]
c = [[1 for _ in range(h)] for _ in range(w)]
# 塗りつぶされた部分を1にしていく
for xya in xyas:
    x, y, a = xya[0], xya[1], xya[2]
    if a == 1:
        for i in range(x):
            c[i] = [0 for _ in range(h)]
    elif a == 2:
        for i in range(x, w):
            c[i] = [0 for _ in range(h)]
    elif a == 3:
        for i in range(w):
            for j in range(y):
                c[i][j] = 0
    elif a == 4:
        for i in range(w):
            for j in range(y, h):
                c[i][j] = 0

print((sum([sum(c2) for c2 in c])))

