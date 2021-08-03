from fractions import Fraction
# from math import ceil

s, x1, x2 = [int(v) for v in input().split()]
t1, t2 = [int(v) for v in input().split()]
p, d = [int(v) for v in input().split()]

# s, x1, x2 = 4,2,4
# t1, t2 = 3,4
# p, d = 1,1

# s, x1, x2 = 5,4,0
# t1, t2 = 1,2
# p, d = 3,1

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
    # print('a')
    print((x2 - x1) * t2)
else:
    # tram=t1, igor=t2
    # t = (x1 - p) * (t1 * t2) / (t2 - t1)
    meet = x1 + Fraction((x1 - p) * t1, t2 - t1)
    if x1 <= meet < x2:
        # print('b')
        print((x1 - p) * t1 + (x2 - x1) * t1)
    else:
        # print('c')
        print((x2 - x1) * t2)
