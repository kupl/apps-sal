(x1, y1, x2, y2) = map(int, input().split())
(a, b) = map(int, input().split())
x = (x1 - x2) / a
y = (y1 - y2) / b
if x == int(x) and y == int(y) and (int(x) & 1 == int(y) & 1):
    print('YES')
else:
    print('NO')
