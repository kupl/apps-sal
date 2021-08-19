# https://note.nkmk.me/python-gcd-lcm/
import math
from functools import reduce


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


n, x = map(int, input().split())
a = list(map(int, input().split()))
tmp = []
for i in range(n):
    tmp.append(abs(a[i] - x))

print(gcd_list(tmp))
