(x1, y1, x2, y2) = list(map(int, input().split()))
(x3, y3, x4, y4) = list(map(int, input().split()))
(x5, y5, x6, y6) = list(map(int, input().split()))
f = False
if x3 <= x1 <= x4 and x3 <= x2 <= x4:
    if y3 <= y1 <= y4 and y3 <= y2 <= y4:
        f = True
    elif y1 < y3 <= y2 <= y4:
        y2 = y3
    elif y3 <= y1 <= y4 < y2:
        y1 = y4
if y3 <= y1 <= y4 and y3 <= y2 <= y4:
    if x3 <= x1 <= x4 and x3 <= x2 <= x4:
        f = True
    elif x1 < x3 <= x2 <= x4:
        x2 = x3
    elif x3 <= x1 <= x4 < x2:
        x1 = x4
if x5 <= x1 <= x6 and x5 <= x2 <= x6:
    if y5 <= y1 <= y6 and y5 <= y2 <= y6:
        f = True
print('NO' if f else 'YES')
