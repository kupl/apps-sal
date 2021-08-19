def main():
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    c = tuple(map(int, input().split()))
    (a, b, c) = sorted((a, b, c))
    (x1, y1) = a
    (x2, y2) = b
    (x3, y3) = c
    dy2 = y2 - y1
    dy3 = y3 - y1
    sy2 = 1 if dy2 >= 0 else -1
    sy3 = 1 if dy3 >= 0 else -1
    ay2 = abs(dy2)
    ay3 = abs(dy3)
    c = 0
    res = []
    if sy2 == sy3:
        for i in range(x1, x2 + 1):
            c += 1
            res.append((i, y1))
        for i in range(1, max(ay2, ay3) + 1):
            c += 1
            res.append((x2, y1 + sy2 * i))
        for i in range(x2 + 1, x3 + 1):
            c += 1
            res.append((i, y3))
    else:
        for i in range(x1, x3 + 1):
            c += 1
            res.append((i, y1))
        for i in range(1, ay2 + 1):
            c += 1
            res.append((x2, y1 + sy2 * i))
        for i in range(1, ay3 + 1):
            c += 1
            res.append((x3, y1 + sy3 * i))
    print(c)
    for (x, y) in res:
        print(x, y)


main()
