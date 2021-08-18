def get_ans(x1, y1, x2, y2):
    def_x = abs(x2 - x1)
    def_y = abs(y2 - y1)

    if x2 < x1 and y2 <= y1:
        x3 = x2 + def_y
        y3 = y2 - def_x
        x4 = x1 + def_y
        y4 = y1 - def_x
    elif y2 < y1 and x1 <= x2:
        x3 = x2 + def_y
        y3 = y2 + def_x
        x4 = x1 + def_y
        y4 = y1 + def_x
    elif x2 > x1 and y1 <= y2:
        x3 = x2 - def_y
        y3 = y2 + def_x
        x4 = x1 - def_y
        y4 = y1 + def_x
    elif y2 > y1 and x1 >= x2:
        x3 = x2 - def_y
        y3 = y2 - def_x
        x4 = x1 - def_y
        y4 = y1 - def_x

    print(x3, y3, x4, y4)


x1, y1, x2, y2 = map(int, input().split())
get_ans(x1, y1, x2, y2)
