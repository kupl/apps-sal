(w, h, n) = map(int, input().split())
(r, l, u, d) = (w, 0, h, 0)
for _ in range(n):
    (x, y, a) = map(int, input().split())
    if a == 1:
        l = max(l, x)
    elif a == 2:
        r = min(r, x)
    elif a == 3:
        d = max(d, y)
    else:
        u = min(u, y)
print(max(0, r - l) * max(0, u - d))
