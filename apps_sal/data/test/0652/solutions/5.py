from collections import Counter


def read_ints():
    return [int(x) for x in input().split()]


def main():
    n, = read_ints()
    points = []
    for i in range(0, n):
        x, y = read_ints()
        points.append((x, y))

    c = Counter()
    for i in range(0, n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            c[(x1 + x2, y1 + y2)] += 1
    res = 0
    for k, v in c.items():
        res += v * (v - 1)
    res //= 2
    print(res)


main()
