for i in range(int(input())):
    (x, y, p, q) = map(int, input().split())
    print(-(x > 0) if not p else -(y > x) if p == q else max((x - 1) // p, (y - x - 1) // (q - p)) * q + q - y)
