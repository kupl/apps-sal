import sys
import math
from functools import reduce

n, k = map(int, input().split())
x = list(map(int, input().split()))

l = []

for i in x:
    b = abs(i - k)
    l.append(b)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


ans = (gcd_list(l))

print(ans)
