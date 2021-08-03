for _ in range(int(input())):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    dx, dy = x2 - x1, y2 - y1
    if dx < 0 or dy < 0:
        print(0)
    else:
        print(dx * dy + 1)
