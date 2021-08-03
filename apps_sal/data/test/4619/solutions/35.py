w, h, n = map(int, input().split())
b = w
c = h
d = 0
e = 0
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        d = max(x, d)
    elif a == 2:
        b = min(x, b)
    elif a == 3:
        e = max(y, e)
    elif a == 4:
        c = min(y, c)
if b < d or c < e:
    print(0)
else:
    print((b - d) * (c - e))
