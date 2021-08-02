def srch(d1af, d2af):

    rtm = int(1e16)
    for i1 in range(n + 1):
        r1m = d1af[i1]
        r2m = int(0)

        for i2 in range(n + 1):
            if d1af[i2] <= r1m:
                None
            else:
                r2m = max(r2m, d2af[i2])

        rtm = min(rtm, r1m + r2m)

    return rtm


n, x1, y1, x2, y2 = list(map(int, input().split()))

d1a = [0]
d2a = [0]

for _ in range(n):
    x, y = list(map(int, input().split()))

    d1 = (x - x1) ** 2 + (y - y1) ** 2
    d2 = (x - x2) ** 2 + (y - y2) ** 2

    d1a.append(d1)
    d2a.append(d2)

print(srch(d1a, d2a))
# PYPY!!!
