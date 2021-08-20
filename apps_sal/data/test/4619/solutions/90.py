(w, h, n) = map(int, input().split())
a = [[int(i) for i in input().split()] for i in range(n)]
(x, y) = (0, 0)
for (s, t, u) in a:
    if u == 1:
        x = max(x, s)
    elif u == 2:
        w = min(w, s)
    elif u == 3:
        y = max(y, t)
    else:
        h = min(h, t)
height = max(0, h - y)
width = max(0, w - x)
print(height * width)
