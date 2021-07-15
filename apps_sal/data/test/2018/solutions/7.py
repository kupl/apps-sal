import math

(n, m, q) = list(map(int, input().split(' ')))
lcm = n * m // math.gcd(n, m)

for i in range(0, q):
    (x1, y1, x2, y2) = list(map(int, input().split(' ')))
    p1 = int(0)
    p2 = int(0)
    if x1 == 1:
        p1 = y1 * m
    else:
        p1 = y1 * n
    if x2 == 1:
        p2 = y2 * m
    else:
        p2 = y2 * n
    if ((p1 - 1) // lcm) == ((p2 - 1) // lcm):
        print('YES')
    else:
        print('NO')

