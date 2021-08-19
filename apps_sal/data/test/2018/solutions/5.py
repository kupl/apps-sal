from math import gcd
(n, m, q) = list(map(int, input().split()))
g = gcd(n, m)
(sn, sm) = (n // g, m // g)
for i in range(q):
    (sx, sy, ex, ey) = list(map(int, input().split()))
    if sx == 1:
        t1 = (sy - 1) // sn
    else:
        t1 = (sy - 1) // sm
    if ex == 1:
        t2 = (ey - 1) // sn
    else:
        t2 = (ey - 1) // sm
    if t1 == t2:
        print('YES')
    else:
        print('NO')
