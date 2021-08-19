import sys
input = sys.stdin.readline
(x1, y1, x2, y2) = list(map(int, input().split()))
(x3, y3, x4, y4) = list(map(int, input().split()))
(x5, y5, x6, y6) = list(map(int, input().split()))


def cut(x1, y1, x2, y2, x3, y3, x4, y4):
    if x3 <= x1 and x2 <= x4:
        if y3 <= y1 <= y4:
            y1 = min(y2, y4)
        if y3 <= y2 <= y4:
            y2 = max(y1, y3)
    if y3 <= y1 and y2 <= y4:
        if x3 <= x1 <= x4:
            x1 = min(x2, x4)
        if x3 <= x2 <= x4:
            x2 = max(x1, x3)
    return (x1, y1, x2, y2)


(x1, y1, x2, y2) = cut(x1, y1, x2, y2, x3, y3, x4, y4)
(x1, y1, x2, y2) = cut(x1, y1, x2, y2, x5, y5, x6, y6)
if x1 == x2 or y1 == y2:
    print('NO')
else:
    print('YES')
