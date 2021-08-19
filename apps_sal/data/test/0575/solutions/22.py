n = int(input())
(ax, ay) = [int(s) for s in input().split()]
(bx, by) = [int(s) for s in input().split()]
(cx, cy) = [int(s) for s in input().split()]
if (bx - ax < 0 and cx - ax < 0 or (bx - ax > 0 and cx - ax > 0)) and (by - ay < 0 and cy - ay < 0 or (by - ay > 0 and cy - ay > 0)):
    print('YES')
else:
    print('NO')
