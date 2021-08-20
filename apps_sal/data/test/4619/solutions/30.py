(w, h, n) = list(map(int, input().split()))
sw = 0
sh = 0
for _ in range(n):
    (x, y, a) = list(map(int, input().split()))
    if a == 1:
        sw = max(sw, x)
    elif a == 2:
        w = min(w, x)
    elif a == 3:
        sh = max(sh, y)
    elif a == 4:
        h = min(h, y)
if sw < w and sh < h:
    print((w - sw) * (h - sh))
else:
    print(0)
