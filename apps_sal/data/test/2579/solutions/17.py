from sys import stdin
from math import ceil
from math import floor

l, r, x, y, k = list(map(int, stdin.readline().split()))
L = max(l, k * x)
R = min(r, k * y)

L = ceil(L / k)
R = floor(R / k)
print('YES' if R >= L else 'NO')

