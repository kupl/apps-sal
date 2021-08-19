import math


def dotproduct(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    product = x1 * x2 + y1 * y2
    return product


def crossproduct(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    product = x1 * y2 - y1 * x2
    return product


def magnitude(x, y):
    mag = math.sqrt(x ** 2 + y ** 2)
    return mag


def main():
    magnitudes = []
    (n, x0, y0) = list(map(int, input().split()))
    x = x0
    y = y0
    for i in range(n):
        (x2, y2) = list(map(int, input().split()))
        x2 = x2 - x0
        y2 = y2 - y0
        if i == 0:
            x1 = x2
            y1 = y2
            x = x2
            y = y2
        magnitudes.append(magnitude(x2, y2))
        dot1 = dotproduct([x, y], [x - x2, y - y2])
        dot2 = dotproduct([x2, y2], [x2 - x, y2 - y])
        if dot1 * dot2 > 0:
            total = abs(crossproduct([x, y], [x2 - x, y2 - y]) / magnitude(x - x2, y - y2))
            magnitudes.append(total)
        x = x2
        y = y2
    dot3 = dotproduct([x, y], [x - x1, y - y1])
    dot4 = dotproduct([x1, y1], [x1 - x, y1 - y])
    if dot3 * dot4 > 0:
        total1 = abs(crossproduct([x, y], [x1 - x, y1 - y]) / magnitude(x - x1, y - y1))
        magnitudes.append(total1)
    print((max(magnitudes) ** 2 - min(magnitudes) ** 2) * 3.141592653589793)


def __starting_point():
    main()


__starting_point()
