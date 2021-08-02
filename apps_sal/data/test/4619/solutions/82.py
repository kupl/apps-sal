w, h, n = map(int, input().split())
l, r, t, b = 0, w, h, 0
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        l = max(x, l)
    elif a == 2:
        r = min(x, r)
    elif a == 3:
        b = max(y, b)
    else:
        t = min(y, t)
if (r - l) <= 0 or (t - b) <= 0:
    print(0)
else:
    print((r - l) * (t - b))
