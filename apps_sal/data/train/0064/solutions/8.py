from bisect import bisect_right
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    (n, l) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    c1 = []
    speed = 1
    x = 0
    t = 0.0
    for a in A:
        t += (a - x) / speed
        c1.append(t)
        speed += 1
        x = a
    c2 = []
    speed = 1
    x = l
    t = 0.0
    for a in reversed(A):
        t += (x - a) / speed
        c2.append(t)
        speed += 1
        x = a
    lo = 0.0
    hi = float(l)
    while hi - lo > 1e-07:
        m = (lo + hi) / 2
        i1 = bisect_right(c1, m) - 1
        if i1 == -1:
            x1 = m
        else:
            tpass = c1[i1]
            textra = m - tpass
            x1 = A[i1] + textra * (i1 + 2)
        i2 = bisect_right(c2, m) - 1
        if i2 == -1:
            x2 = l - m
        else:
            tpass = c2[i2]
            textra = m - tpass
            x2 = A[-1 - i2] - textra * (i2 + 2)
        if x1 < x2:
            lo = m
        else:
            hi = m
    print((lo + hi) / 2)
