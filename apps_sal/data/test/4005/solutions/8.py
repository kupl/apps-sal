(x1, y1, x2, y2) = map(int, input().split())
(x3, y3, x4, y4) = map(int, input().split())
(x5, y5, x6, y6) = map(int, input().split())
if y1 >= y3 and y2 <= y4 and (x1 >= x3) and (x2 <= x4):
    print('NO')
elif y1 >= y5 and y2 <= y6 and (x1 >= x5) and (x2 <= x6):
    print('NO')
elif x3 <= x1 and x4 >= x2 and (x5 <= x1) and (x6 >= x2) and (y3 <= y1 <= y5 <= y4 <= y2 <= y6):
    print('NO')
elif x3 <= x1 and x4 >= x2 and (x5 <= x1) and (x6 >= x2) and (y5 <= y1 <= y3 <= y6 <= y2 <= y4):
    print('NO')
elif y3 <= y1 and y4 >= y2 and (y5 <= y1) and (y6 >= y2) and (x3 <= x1 <= x5 <= x4 <= x2 <= x6):
    print('NO')
elif y3 <= y1 and y4 >= y2 and (y5 <= y1) and (y6 >= y2) and (x5 <= x1 <= x3 <= x6 <= x2 <= x4):
    print('NO')
else:
    print('YES')
