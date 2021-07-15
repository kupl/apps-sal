from functools import reduce
from math import gcd
n = int(input())
xlist = list(map(int,input().split()))
print(reduce(gcd, xlist))
