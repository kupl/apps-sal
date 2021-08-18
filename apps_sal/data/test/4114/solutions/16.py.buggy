n, *xyh = map(int, open(0).read().split())
a = sorted([(xyh[i * 3], xyh[i * 3 + 1], xyh[i * 3 + 2]) for i in range(n)], key=lambda x: x[2], reverse=True)
for i in range(101):
    for j in range(101):
        dh = abs(a[0][0] - i) + abs(a[0][1] - j) + a[0][2]
        for x, y, h in a[1:]:
            if h != max(dh - abs(x - i) - abs(y - j), 0):
                break
        else:
            print(i, j, dh)
            return
