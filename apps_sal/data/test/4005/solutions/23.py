x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
x5, y5, x6, y6 = list(map(int, input().split()))
z = 0
if x3 <= x1 and x4 >= x2 and y3 <= y1 and y4 >= y2:
    z = 1
if x5 <= x1 and x6 >= x2 and y5 <= y1 and y6 >= y2:
    z = 1
if y3 > y5:
    if y3 <= y6 and y4 >= y2 and y5 <= y1:
        if x3 <= x1 and x4 >= x2 and x5 <= x1 and x6 >= x2:
            z = 1
else:
    y3, y5 = y5, y3
    y6, y4 = y4, y6
    if y3 <= y6 and y4 >= y2 and y5 <= y1:
        if x3 <= x1 and x4 >= x2 and x5 <= x1 and x6 >= x2:
            z = 1
y3, y5 = y5, y3
y6, y4 = y4, y6
if x3 < x5:
    if x3 <= x1 and x4 >= x5 and x6 >= x2:
        if y3 <= y1 and y4 >= y2 and y5 <= y1 and y6 >= y2:
            z = 1
else:
    x3, x5 = x5, x3
    x6, x4 = x4, x6
    if x3 <= x1 and x4 >= x5 and x6 >= x2:
        if y3 <= y1 and y4 >= y2 and y5 <= y1 and y6 >= y2:
            z = 1
if z == 1:
    print("NO")
else:
    print("YES")
