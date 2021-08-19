import math
from functools import reduce
(n, x) = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
b = []
for i in range(len(a) - 1):
    b.append(abs(a[i] - a[i - 1]))


def gcd(*numbers):
    return reduce(math.gcd, numbers)


print(gcd(*b))
