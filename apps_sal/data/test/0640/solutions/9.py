import math
(a, b) = list(map(int, input().split()))
(win1, draw, win2) = (0, 0, 0)
for i in range(1, 7):
    c = math.fabs(a - i)
    d = math.fabs(b - i)
    if c < d:
        win1 += 1
    elif c == d:
        draw += 1
    else:
        win2 += 1
print(win1, draw, win2)
