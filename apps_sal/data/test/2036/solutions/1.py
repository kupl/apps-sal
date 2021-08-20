(w, h, sx, sy) = list(map(int, input().split()))
for x in range(sx, w + 1):
    for y in range(sy, h + 1):
        print(x, y)
    for y in range(1, sy):
        print(x, y)
    sy = y
for x in range(1, sx):
    for y in range(sy, h + 1):
        print(x, y)
    for y in range(1, sy):
        print(x, y)
    sy = y
