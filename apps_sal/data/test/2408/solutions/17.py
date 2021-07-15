n = int(input())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


poles = []
for i in range(n):
    x, y = list(map(int, input().split()))
    poles.append((x, y))

lines = set()
for i in range(len(poles) - 1):
    for j in range(i + 1, len(poles)):
        p1 = poles[i]
        p2 = poles[j]
        a = p1[1] - p2[1]
        b = - p1[0] + p2[0]
        abg = gcd(abs(a), abs(b))
        if abg > 0:
            a //= abg
            b //= abg
        if a < 0:
            a = -a
            b = -b
        if a == 0:
            b = 1
        if b == 0:
            a = 1
        c = - a * p1[0] - b * p1[1]
        lines.add((a, b, c))
        # print(a, b, c)

        # lines.append((p1, p2))

# points = set()
cnt = 0
for i, line1 in enumerate(lines):
    for j, line2 in enumerate(lines):
        if i >= j:
            continue
        # print(i, j)

        if line1[:2] != line2[:2]:
            cnt += 1

        # ap1 = line1[0]
        # ap2 = line1[1]
        # bp1 = line2[0]
        # bp2 = line2[1]
        #
        # under = (bp2[1] - bp1[1]) * (ap2[0] - ap1[0]) - (bp2[0] - bp1[0]) * (ap2[1] - ap1[1])
        # if under == 0:
        #     continue
        #
        # t = (bp2[0] - bp1[0]) * (ap1[1] - bp1[1]) - (bp2[1] - bp1[1]) * (ap1[0] - bp1[0])
        # s = (ap2[0] - ap1[0]) * (ap1[1] - bp1[1]) - (ap2[1] - ap1[1]) * (ap1[0] - bp1[0])
        #
        # if t < 0 or t > under or s < 0 or s > under:
        #     continue
        #
        # if t == 0 and s == 0:
        #     continue
        #
        # print('add')
        # cnt += 1

        # x = [ap1[0] * under + t * (ap2[0] - ap1[0]), under]
        # y = [ap1[1] * under + t * (ap2[1] - ap1[1]), under]
        # xg = gcd(x[0], x[1])
        # if xg > 0:
        #     x[0] //= xg
        #     x[1] //= xg
        # yg = gcd(y[0], y[1])
        # if yg > 0:
        #     y[0] //= yg
        #     y[1] //= yg
        # if under < 0:
        #     x[0] = -x[0]
        #     x[1] = -x[1]
        #     y[0] = -y[0]
        #     y[1] = -y[1]
        #
        # x = tuple(x)
        # y = tuple(y)
        # p = (x, y)
        #
        #
        #

print(cnt)

