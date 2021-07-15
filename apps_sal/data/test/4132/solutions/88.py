from functools import reduce
from math import gcd

n = int(input())
a = list(map(int,input().split()))
g = reduce(gcd,a)
print(g)
