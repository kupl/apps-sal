from fractions import gcd
from functools import reduce
N = input()

List = list(map(int, input().split()))

print((reduce(gcd, List)))

