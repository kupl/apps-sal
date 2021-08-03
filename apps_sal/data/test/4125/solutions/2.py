import math
from functools import reduce


def gcd(numbers):
    return reduce(math.gcd, numbers)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.append(a[1])
c = sorted(b)
d = []
for i in range(a[0]):
    d.append(c[i + 1] - c[i])
print(gcd(d))
