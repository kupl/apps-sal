from fractions import gcd
from functools import reduce
n = int(input())
a = list(map(int, input().split()))
print(n * reduce(gcd, a))
