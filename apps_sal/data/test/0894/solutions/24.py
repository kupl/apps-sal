while 1:
    try:
        (x, y) = map(int, input().split())
        if x > 0 and y > 0:
            (x1, y1, x2, y2) = (0, x + y, x + y, 0)
        elif x < 0 and y > 0:
            (x1, y1, x2, y2) = (-(-x + y), 0, 0, -x + y)
        elif x < 0 and y < 0:
            (x1, y1, x2, y2) = (-(-x - y), 0, 0, -(-x - y))
        else:
            (x1, y1, x2, y2) = (0, -(x - y), x - y, 0)
        print(x1, y1, x2, y2, end=' ')
    except EOFError:
        break
