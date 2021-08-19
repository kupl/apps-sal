(x1, y1, x2, y2) = list(map(int, input().split()))
(x, y) = list(map(int, input().split()))
if abs(x1 - x2) % x != 0 or abs(y1 - y2) % y != 0:
    print('NO')
else:
    a = abs(x1 - x2) / x
    b = abs(y1 - y2) / y
    if a % 2 == b % 2:
        print('YES')
    else:
        print('NO')
