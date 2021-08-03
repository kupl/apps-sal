from math import *
s, x1, x2 = map(int, input().split())
t1, t2 = map(int, input().split())
p, d = map(int, input().split())
ans = abs(x1 - x2) * t2
if t1 >= t2:
    print(ans)

elif x1 <= x2:
    if d == 1:
        if p <= x1:
            print(min(ans, t1 * (x2 - p)))
        else:
            print(min(ans, t1 * (s - p + s + x2)))
    else:
        print(min(ans, t1 * (p + x2)))
else:

    if d == 1:

        print(min(ans, t1 * (s - p + (s - x2))))

    else:
        if p >= x1:
            print(min(ans, t1 * (p - x2)))
        else:
            print(min(ans, t1 * (s + p + (s - x2))))
