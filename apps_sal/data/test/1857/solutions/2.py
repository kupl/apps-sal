from functools import reduce
from math import factorial
n = int(input())
def C_n_k(n, k): return reduce(lambda x, y: x * y, list(range(n, n - k, -1))) // factorial(k)


print((C_n_k(n, 5) ** 2) * 120)
