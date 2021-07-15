from functools import reduce
from operator import mul

print((reduce(mul, (i * (1 + i) // 2 for i in map(int, input().split()))) % 998244353))

