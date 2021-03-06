import sys
from math import gcd
reader = (list(map(int, s.split())) for s in sys.stdin)
(t,) = next(reader)
for _ in range(t):
    (r, b, k) = next(reader)
    if r > b:
        (r, b) = (b, r)
    g = gcd(r, b)
    seq = (b - g - 1) // r + 1
    print('OBEY' if seq < k else 'REBEL')
