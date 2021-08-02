from functools import reduce
from math import gcd
n = int(input())
L = list(map(int, input().split()))


ans = reduce(gcd, L)
print(ans)
