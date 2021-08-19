def main():
    (n, a, b) = [int(t) for t in input().split()]
    points = []
    for _ in range(n):
        point = [int(t) for t in input().split()]
        points.append(point)
    largest_area = 0
    for (i, (x1, y1)) in enumerate(points):
        for (j, (x2, y2)) in enumerate(points):
            if i == j:
                continue
            if satisfy(x1, y1, x2, y2, a, b):
                area = x1 * y1 + x2 * y2
                largest_area = max(area, largest_area)
    print(largest_area)


def satisfy(x1, y1, x2, y2, a, b):
    if satisfy_single(max((x1, x2)), sum((y1, y2)), a, b):
        return True
    if satisfy_single(sum((x1, x2)), max((y1, y2)), a, b):
        return True
    if satisfy_single(max((x1, y2)), sum((y1, x2)), a, b):
        return True
    if satisfy_single(sum((x1, y2)), max((y1, x2)), a, b):
        return True
    if satisfy_single(max((y1, x2)), sum((x1, y2)), a, b):
        return True
    if satisfy_single(sum((y1, x2)), max((x1, y2)), a, b):
        return True
    return False


def satisfy_single(x, y, a, b):
    if x <= a and y <= b:
        return True
    if x <= b and y <= a:
        return True
    return False


def __starting_point():
    main()


__starting_point()
