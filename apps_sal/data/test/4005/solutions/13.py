def ll():
    return list(map(int, input().split()))


testcases = 1
for _ in range(testcases):
    [x1, y1, x2, y2] = ll()
    [x3, y3, x4, y4] = ll()
    [x5, y5, x6, y6] = ll()

    def lies1(x0, y0):
        return x0 >= x3 and x0 <= x4 and (y0 >= y3) and (y0 <= y4)

    def lies2(x0, y0):
        return x0 >= x5 and x0 <= x6 and (y0 >= y5) and (y0 <= y6)

    def lies(x0, y0):
        return lies1(x0, y0) or lies2(x0, y0)
    ap = [[x1, y1], [x2, y2], [x1, y2], [x2, y1]]
    ok = 1
    for x in ap:
        if not lies(x[0], x[1]):
            ok = 0
            break
    else:
        if x1 >= max(x3, x5) and x2 <= min(x4, x6):
            if y1 <= y6 and y6 < y3 and (y3 <= y2) or (y1 <= y4 and y4 < y5 and (y5 <= y2)):
                ok = 0
        elif x1 <= x6 and x6 < x3 and (x3 <= x2) or (x1 <= x4 and x4 < x5 and (x5 <= x2)):
            ok = 0
    if ok:
        print('NO')
    else:
        print('YES')
