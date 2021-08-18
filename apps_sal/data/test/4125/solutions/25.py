from functools import reduce
from fractions import gcd

N, X = list(map(int, input().split()))
x = list(map(int, input().split()))
res = list(abs(i - X) for i in x)

print((reduce(gcd, res)))
