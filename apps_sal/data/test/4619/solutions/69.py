w, h, n = map(int, input().split())
b = [0, 0]
c = [w, h]
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        if b[0] < x:
            b[0] = x
    elif a == 2:
        if c[0] > x:
            c[0] = x
    elif a == 3:
        if b[1] < y:
            b[1] = y
    else:
        if c[1] > y:
            c[1] = y
d = max(0, (c[0] - b[0])) * max(0, (c[1] - b[1]))
print(d)
