t = int(input())
for i in range(t):
    (a, b, c, d) = list(map(int, input().split()))
    (x, y, x1, y1, x2, y2) = list(map(int, input().split()))
    x += b - a
    y += d - c
    u = a + b
    e = c + d
    if x >= x1 and x <= x2 and (y <= y2) and (y >= y1) and (not (u != 0 and x1 == x2)) and (not (e != 0 and y1 == y2)):
        print('Yes')
    else:
        print('No')
