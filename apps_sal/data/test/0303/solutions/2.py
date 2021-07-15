x1, y1, x2, y2 = map(int, input().split())
a, b = map(int, input().split())
if not abs(x1 - x2) % a and not abs(y1 - y2) % b and (abs(x1 - x2) // a) % 2 == (abs(y1 - y2) // b) % 2:
    print('YES')
else:
    print('NO')
