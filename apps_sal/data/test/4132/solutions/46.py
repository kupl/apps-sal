from math import gcd
from functools import reduce
n = int(input())
A = list(map(int, input().split()))
def GCD(*numbers):
    return reduce(gcd, numbers)
g = GCD(*A)
print(g)

