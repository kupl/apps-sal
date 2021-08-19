import math
(n, m, q) = list(map(int, input().split()))
g = math.gcd(n, m)
for qq in range(q):
    (a, b, c, d) = list(map(int, input().split()))
    if a == 1:
        x = (b - 1) // (n // g)
    else:
        x = (b - 1) // (m // g)
    if c == 1:
        y = (d - 1) // (n // g)
    else:
        y = (d - 1) // (m // g)
    if x == y:
        print('YES')
    else:
        print('NO')
