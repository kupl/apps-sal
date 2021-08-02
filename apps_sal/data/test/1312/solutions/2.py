# A
from math import ceil, floor
n, m = list(map(int, input().split()))
L = []
if not n % m:
    for _ in range(m):
        L.append(n // m)
else:
    MIN = floor(n / m)
    MAX = ceil(n / m)
    for _ in range(n % m):
        L.append(MAX)
    for _ in range(m - (n % m)):
        L.append(MIN)

print(' '.join(map(str, L)))
