(x1, y1, x2, y2) = map(int, input().split())
(x, y) = map(int, input().split())
(x, y) = (abs(x), abs(y))
x_ = abs(x2 - x1)
y_ = abs(y2 - y1)
if x_ % x == 0 and y_ % y == 0:
    if (x_ // x + y_ // y) % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
