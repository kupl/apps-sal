x1, y1, x2, y2 = list(map(int, input().split()))
x, y = list(map(int, input().split()))
dx, dy = x1-x2, y1-y2
if dx%x == 0 and dy%y == 0 and (dx//x + dy//y)%2 == 0:
    print('YES')
else:
    print('NO')

