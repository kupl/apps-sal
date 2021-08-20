import math
(n, m, q) = list(map(int, input().split()))
d = math.gcd(n, m)
(nd, md) = (n // d, m // d)
for _ in range(q):
    (x, y, u, v) = list(map(int, input().split()))
    y -= 1
    v -= 1
    if x == 1:
        y //= nd
    else:
        y //= md
    if u == 1:
        v //= nd
    else:
        v //= md
    if y == v:
        print('YES')
    else:
        print('NO')
