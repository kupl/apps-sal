from math import gcd
from functools import reduce


def gcd_list(a):
    ans = reduce(gcd, a)
    return ans


n = int(input())
a = list(map(int, input().split()))
mn = min(a)
a = [el - mn for el in a]
z = gcd_list(a)
mx = max(a)
y = 0
for el in a:
    y += (mx - el) // z
print(y, z)

