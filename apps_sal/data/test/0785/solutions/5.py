from math import *
from itertools import *
(n, a, b) = map(int, input().split())
if a * b >= 6 * n:
    print(a * b)
    print(a, b)
else:
    p = ceil(sqrt(6 * n))
    (s, a1, b1) = min(chain(((x * ceil(6 * n / x), x, ceil(6 * n / x)) for x in range(a, p + 1) if ceil(6 * n / x) >= b), ((ceil(6 * n / y) * y, ceil(6 * n / y), y) for y in range(b, p + 1) if ceil(6 * n / y) >= a)))
    print(s)
    print(a1, b1)
