from functools import reduce
from fractions import gcd

N, X = list(map(int, input().split()))
x = list(map(int, input().split()))
res = list(abs(i - X) for i in x)

# resの最大公約数を求める。　コードは reduce(gcd, list)
print((reduce(gcd, res)))
