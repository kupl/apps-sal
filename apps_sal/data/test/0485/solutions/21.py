def find_inside_point(points, maxx, minx, maxy, miny):
    for x, y in points:
        if minx < x < maxx and miny < y < maxy:
            print(x, y)
            return


def find_outside_point(points, maxx, minx, maxy, miny):
    maxx_points = [(x, y) for x, y in points if x == maxx]
    minx_points = [(x, y) for x, y in points if x == minx]
    maxy_points = [(x, y) for x, y in points if y == maxy]
    miny_points = [(x, y) for x, y in points if y == miny]

    if len(maxx_points) == 1:
        print(*maxx_points[0])
    elif len(minx_points) == 1:
        print(*minx_points[0])
    elif len(maxy_points) == 1:
        print(*maxy_points[0])
    else:
        print(*miny_points[0])


def process(n, points):
    xs, ys = [x for x, _ in points], [y for _, y in points]
    maxx, minx = max(xs), min(xs)
    maxy, miny = max(ys), min(ys)

    if maxx - minx == maxy - miny:
        find_inside_point(points, maxx, minx, maxy, miny)
    else:
        find_outside_point(points, maxx, minx, maxy, miny)


def __starting_point():
    n = int(input())
    points = []

    for _ in range(4 * n + 1):
        x, y = [int(z) for z in input().split()]
        points.append((x, y))

    process(n, points)


__starting_point()
