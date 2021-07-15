from itertools import *
from math import *
n, m = map(int, input().split())
x, y = (max(1, ceil(log(k, 7))) for k in [n, m])
p = [''.join(t) for t in permutations('0123456', x + y)]
print(0 if x + y > 7 else sum(int(t[:x], 7) < n and int(t[x:], 7) < m for t in p))
