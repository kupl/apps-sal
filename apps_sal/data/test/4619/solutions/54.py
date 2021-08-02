w, h, n = list(map(int, input().split()))
ox, oy = 0, 0
for i in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        if ox < x:
            ox = x
    elif a == 2:
        if w > x:
            w = x
    elif a == 3:
        if oy < y:
            oy = y
    else:
        if h > y:
            h = y
print((max(w - ox, 0) * max(h - oy, 0)))
