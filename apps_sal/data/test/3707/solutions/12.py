from fractions import Fraction as F
from math import ceil, floor
(n, t, k, d) = map(int, input().split())
single = t * ceil(F(n, k))
double1 = k * floor(F(single - 1, t))
double2 = max(0, k * floor(F(single - d - 1, t)))
print('YES' if double1 + double2 >= n else 'NO')
