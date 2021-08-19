n = int(input())
(ax, ay) = list(map(int, input().split()))
(bx, by) = list(map(int, input().split()))
(cx, cy) = list(map(int, input().split()))
x = [ax, bx, cx]
y = [ay, by, cy]
x.sort()
y.sort()
if x[1] != ax and y[1] != ay:
    print('YES')
else:
    print('NO')
