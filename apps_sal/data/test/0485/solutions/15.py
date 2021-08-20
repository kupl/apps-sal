n = int(input())
points = list((tuple(map(int, input().split())) for i in range(4 * n + 1)))
xs = list(sorted(points))
ys = list(sorted(points, key=lambda x: (x[1], x[0])))
xsize = xs[-1][0] - xs[0][0]
ysize = ys[-1][1] - ys[0][1]


def check(point):
    p1 = xs[-1][0] if xs[-1] != point else xs[-2][0]
    p2 = xs[0][0] if xs[0] != point else xs[1][0]
    p3 = ys[-1][1] if ys[-1] != point else ys[-2][1]
    p4 = ys[0][1] if ys[0] != point else ys[1][1]
    return p1 - p2 == p3 - p4


if xsize == ysize:
    for p in points:
        if p[0] != xs[0][0] and p[0] != xs[-1][0] and (p[1] != ys[-1][1]) and (p[1] != ys[0][1]):
            print(p[0], p[1])
elif check(xs[-1]):
    print(xs[-1][0], xs[-1][1])
elif check(xs[0]):
    print(xs[0][0], xs[0][1])
elif check(ys[-1]):
    print(ys[-1][0], ys[-1][1])
elif check(ys[0]):
    print(ys[0][0], ys[0][1])
