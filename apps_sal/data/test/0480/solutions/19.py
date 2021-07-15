s, x1, x2 = list(map(int, input().split()))
t1, t2 = list(map(int, input().split()))
p, d = list(map(int,input().split()))
wt = abs(x2-x1) * t2
if t2 <= t1:
    print(abs(x2-x1) * t2)
    return
tt = 0
if d == 1:
    if p <= x2:
        if x1 <= x2 and p <= x1:
            tt = abs(x2-p)*t1
        elif x1 > x2 and p <= x1:
            tt = (s - p + (s - x2))*t1
        elif x1 < p:
            tt = (s - p + s + x2)*t1
        else:
            raise Exception()
    else:
        if x1 > x2:
            tt = (s - p + s - x2) * t1
        else:
            tt = (s - p + s + x2) * t1
else:
    if p >= x2:
        if x1 >= x2 and p >= x1:
            tt = abs(x2-p)*t1
        elif x1 < x2 and p >= x1:
            tt = (p + x2)*t1
        elif x1 > p:
            tt = (p + s + s - x2)*t1
        else:
            raise Exception()
    else:
        if x1 < x2:
            tt = (p + x2) * t1
        else:
            tt = (p + s + s-x2) * t1

print(min(tt, wt))

