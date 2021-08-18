x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())


def do_mask(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == -1:
        return -1, -1, -1, -1
    if x3 <= x1 and x2 <= x4 and y3 <= y1 and y2 <= y4:
        return -1, -1, -1, -1

    if x3 <= x1 and x2 <= x4:
        if y3 <= y1 and y1 <= y4:
            y1 = y4
        if y3 <= y2 and y2 <= y4:
            y2 = y3

    if y3 <= y1 and y2 <= y4:
        if x3 <= x1 and x1 <= x4:
            x1 = x4
        if x3 <= x2 and x2 <= x4:
            x2 = x3

    return x1, y1, x2, y2


x1, y1, x2, y2 = do_mask(x1, y1, x2, y2, x3, y3, x4, y4)
x1, y1, x2, y2 = do_mask(x1, y1, x2, y2, x5, y5, x6, y6)
print("NO" if x1 == -1 else "YES")
