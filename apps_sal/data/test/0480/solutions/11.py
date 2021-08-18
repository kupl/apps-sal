from fractions import Fraction

s, x1, x2 = [int(v) for v in input().split()]
t1, t2 = [int(v) for v in input().split()]
p, d = [int(v) for v in input().split()]


if x1 > x2:
    x1, x2 = s - x1, s - x2
    p = s - p
    d = -d

if d == -1:
    p = -p
    d = 1
elif d == 1 and p > x1:
    p = -((s - p) + s)


if t2 <= t1:
    print((x2 - x1) * t2)
else:
    meet = x1 + Fraction((x1 - p) * t1, t2 - t1)
    if x1 <= meet < x2:
        print((x1 - p) * t1 + (x2 - x1) * t1)
    else:
        print((x2 - x1) * t2)
