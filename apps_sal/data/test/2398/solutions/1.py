for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())
    if x != x1 or x != x2:
        temp = min(a, b)
        a -= temp
        b -= temp
    if y != y1 or y != y2:
        temp = min(c, d)
        c -= temp
        d -= temp
    flag = 0
    if a > 0:
        if x - a < x1:
            flag = 1
    if b > 0:
        if x + b > x2:
            flag = 1
    if c > 0:
        if y - c < y1:
            flag = 1
    if d > 0:
        if y + d > y2:
            flag = 1
    if flag:
        print("No")
    else:
        print("Yes")
