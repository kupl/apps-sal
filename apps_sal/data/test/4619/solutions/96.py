w, h, n = map(int, input().split())
query = [tuple(map(int, input().split())) for _ in range(n)]

sx, sy = 0, 0
for x, y, a in query:
    if a == 1:
        sx = max(sx, x)
    elif a == 2:
        w = min(w, x)
    elif a == 3:
        sy = max(sy, y)
    else:
        h = min(h, y)
print(max(0, w - sx) * max(0, h - sy))
