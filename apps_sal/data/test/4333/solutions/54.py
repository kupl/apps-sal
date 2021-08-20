(x1, y1, x2, y2) = map(int, input().split())
(x3_1, x3_2) = (x2 - abs(y2 - y1), x2 + abs(y2 - y1))
(x4_1, x4_2) = (x1 - abs(y2 - y1), x1 + abs(y2 - y1))
(y3_1, y3_2) = (y2 - abs(x2 - x1), y2 + abs(x2 - x1))
(y4_1, y4_2) = (y1 - abs(x2 - x1), y1 + abs(x2 - x1))
if x2 > x1 and y2 > y1:
    print(x3_1, y3_2, x4_1, y4_2)
elif x2 > x1 and y2 <= y1:
    print(x3_2, y3_2, x4_2, y4_2)
elif x2 <= x1 and y2 > y1:
    print(x3_1, y3_1, x4_1, y4_1)
elif x2 <= x1 and y2 <= y1:
    print(x3_2, y3_1, x4_2, y4_1)
