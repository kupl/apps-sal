def srch(d1af, d2af):
    rtm = int(0)
    for i1 in range(n):
        r1m = d1af[i1]
        r2m = int(0)
        for i2 in range(n):
            if d1af[i2] <= r1m:
                None
            else:
                r2m = max(r2m, d2af[i2])
        if i1 == 0:
            rtm = r1m + r2m
        else:
            rtm = min(rtm, r1m + r2m)
    return rtm


(n, x1, y1, x2, y2) = list(map(int, input().split()))
r1 = int(0)
r2 = int(0)
d1a = []
d2a = []
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    d1 = abs(x - x1) ** 2 + abs(y - y1) ** 2
    d2 = abs(x - x2) ** 2 + abs(y - y2) ** 2
    d1a.append(d1)
    d2a.append(d2)
rmin = min(srch(d1a, d2a), srch(d2a, d1a))
print(rmin)
