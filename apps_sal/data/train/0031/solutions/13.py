t = int(input())
d = {'E': (1, 0), 'W':(-1, 0), 'N':(0, 1), 'S':(0, -1)}
for _ in range(t):
    s = input()
    time = 0
    met = set()
    x = y = 0
    for c in s:
        dx, dy = d[c]
        xx = x + dx
        yy = y + dy
        if (x, y, xx, yy) in met or (xx, yy, x, y) in met:
            time += 1
        else:
            time += 5
            met.add((x, y, xx, yy))
        x = xx
        y = yy
    print(time)
