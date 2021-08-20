from functools import reduce
from math import gcd
(n, x) = map(int, input().split())
l = [abs(x - int(i)) for i in input().split()]
print(reduce(gcd, l))
