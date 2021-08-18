def resolve():
    a, b, x, y = map(int, input().split())
    if b >= a:
        print((b - a) * min(2 * x, y) + x)
    else:
        print((a - b - 1) * min(2 * x, y) + x)


resolve()
