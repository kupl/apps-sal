[x1, y1, x2, y2] = [int(x) for x in input().split()]
[x3, y3, x4, y4] = [int(x) for x in input().split()]
[x5, y5, x6, y6] = [int(x) for x in input().split()]
no = 'NO'
yes = 'YES'


def ries(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    if x3 <= x1 and y3 <= y1 and (x4 >= x2) and (y4 >= y2):
        return no
    if x5 <= x1 and y5 <= y1 and (x6 >= x2) and (y6 >= y2):
        return no
    if x3 <= x1 and y3 <= y1 and (x4 >= x5) and (y4 >= y2) and (y5 <= y1) and (x6 >= x2) and (y6 >= y2):
        return no
    if x5 <= x1 and y5 <= y1 and (x6 >= x3) and (y6 >= y2) and (y3 <= y1) and (x4 >= x2) and (y4 >= y2):
        return no
    if x3 <= x1 and y3 <= y1 and (x4 >= x2) and (y4 >= y5) and (x5 <= x1) and (x6 >= x2) and (y6 >= y2):
        return no
    if x5 <= x1 and y5 <= y1 and (x6 >= x2) and (y6 >= y3) and (x3 <= x1) and (x4 >= x2) and (y4 >= y2):
        return no
    return yes


print(ries(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6))
