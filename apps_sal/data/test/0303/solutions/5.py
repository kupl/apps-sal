(x1, y1, x2, y2) = list(map(int, input().split()))
(x, y) = list(map(int, input().split()))
if (x2 - x1) % x == 0 and (y2 - y1) % y == 0:
    if ((x2 - x1) // x - (y2 - y1) // y) % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
