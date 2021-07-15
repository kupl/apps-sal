a,b,c = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
if a == 0 or b == 0:
    print(abs(x1 -x2) + abs(y1 - y2))
else:
    a = a / (-b)
    c = c / (-b)
    if (x1 <= x2 and y1 <= y2) or (x1 >= x2 and y1 >= y2):
        y1 = -y1
        y2 = -y2
        a = -a
        c = -c
        x1, x2, y1, y2 = min(x1, x2), max(x1, x2), max(y1, y2), min(y1, y2)
    ax = a
    bx = c
    ay = 1 / a
    by = - c / a
    ans = abs(x1 -x2) + abs(y1 - y2)
    Ax = ay * y1 + by
    Ay = ax * x1 + bx
    Bx = ay * y2 + by
    By = ax * x2 + bx
    ans = min(ans, abs(x1 - Ax) + abs(x2 - Bx) + ((Bx - Ax) ** 2 + (y1 - y2) ** 2)**0.5)
    ans = min(ans, abs(y1 - Ay) + abs(y2 - By) + ((By - Ay) ** 2 + (x1 - x2) ** 2)**0.5)
    ans = min(ans, abs(x1 - Ax) + abs(y2 - By) + ((x2 - Ax) ** 2 + (y1 - By) ** 2)**0.5)
    ans = min(ans, abs(x2 - Bx) + abs(Ay - y1) + ((Bx - x1) ** 2 + (Ay - y2) ** 2)**0.5)
    print(ans)
