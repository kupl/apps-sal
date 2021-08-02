x1, y1, x2, y2 = [int(i) for i in input().split(' ')]
a, b = [int(i) for i in input().split(' ')]

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx % a == 0 and dy % b == 0 and (dx / a) % 2 == (dy / b) % 2:
    print('YES')
else:
    print('NO')
