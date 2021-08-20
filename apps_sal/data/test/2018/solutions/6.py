from math import gcd
(n, m, q) = map(int, input().split())
g = gcd(n, m)
out = []
n //= g
m //= g
for _ in range(q):
    (sx, sy, ex, ey) = map(int, input().split())
    sy -= 1
    ey -= 1
    sp = sy // (n if sx == 1 else m)
    ep = ey // (n if ex == 1 else m)
    out.append('YES' if sp == ep else 'NO')
print(*out, sep='\n')
