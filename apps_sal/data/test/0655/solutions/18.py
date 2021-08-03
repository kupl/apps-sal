n = int(input())
x, y = map(int, input().split())
dx = n - x + 1
dy = n - y + 1
cnt1 = min(x, y) + x - min(x, y) + y - min(x, y)
cnt2 = min(dx, dy) + dx - min(dx, dy) + dy - min(dx, dy)
if cnt1 <= cnt2:
    print('White')
else:
    print('Black')
