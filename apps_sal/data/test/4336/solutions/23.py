(w, h, x, y) = map(int, input().split())
u = w * h / 2
if w == 2 * x and h == 2 * y:
    w = 1
else:
    w = 0
print(u, w)
