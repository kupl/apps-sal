import sys
(s, x1, x2) = list(map(int, sys.stdin.readline().split()))
(t1, t2) = list(map(int, sys.stdin.readline().split()))
(p, d) = list(map(int, sys.stdin.readline().split()))
if x2 > x1:
    dp = 1
else:
    dp = -1
if dp == d:
    if d * p <= d * x1:
        dx2 = abs(x2 - p)
    elif d == 1:
        dx2 = s + (s - p) + x2
    else:
        dx2 = s + p + (s - x2)
elif d == 1:
    dx2 = 2 * s - p - x2
else:
    dx2 = p + x2
tt = dx2 * t1
dx = abs(x1 - x2)
tp = t2 * dx
res = min(tp, tt)
print(res)
