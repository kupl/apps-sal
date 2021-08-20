from math import gcd
(n, m, q) = map(int, input().split())
g = gcd(n, m)
lc = n // g * m
for __ in range(q):
    (sx, sy, ex, ey) = map(int, input().split())
    sy -= 1
    ey -= 1
    sy *= m if sx == 1 else n
    ey *= m if ex == 1 else n
    print('YES' if sy // lc == ey // lc else 'NO')
