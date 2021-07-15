from fractions import gcd
from functools import reduce
print(int(input()) * reduce(gcd, map(int, input().split())))
