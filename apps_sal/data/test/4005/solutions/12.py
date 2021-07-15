x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())
if (y1 > y4 or y1 < y3 or x1 > x4 or x1 < x3) and (y1 < y5 or y1 > y6 or x1 < x5 or x1 > x6):
    print('YES')
elif (y2 > y4 or y2 < y3 or x4 < x2 or x2 < x3) and (y2 < y5 or y2 > y6 or x2 < x5 or x2 > x6):
    print('YES')
elif (y2 > y4 or y2 < y3 or x4 < x1 or x1 < x3) and (y2 < y5 or y2 > y6 or x1 < x5 or x1 > x6):
    print("YES")
elif (y1 > y4 or y1 < y3 or x4 < x2 or x2 < x3) and (y1 < y5 or y1 > y6 or x2 < x5 or x2 > x6):
    print("YES")
elif x5 > x4 and x1 < x5 < x2:
    print("YES")
elif x6 < x3 and x1 < x6 < x2:
    print("YES")
elif y6 < y3 and y1 < y6 < y2:
    print('YES')
elif y5 > y4 and y1 < y5 < y2:
    print('YES')
else:
    print('NO')
