import sys
from collections import Counter
from math import *

for _ in range(int(input())):
    a, b, c, r = map(int, input().split())
    if b < a:
        a, b = b, a
    res1 = max(a, c - r)
    res2 = min(b, c + r)
    print(max(0, b - a - max(0, res2 - res1)))
