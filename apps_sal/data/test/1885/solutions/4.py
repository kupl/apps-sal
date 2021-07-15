from functools import reduce
from math import factorial
n = int(input())
C_n_k = lambda n, k: reduce(lambda x, y: x*y, list(range(n, n-k, -1))) // factorial(k)
print(C_n_k(n, 7) + C_n_k(n, 6) + C_n_k(n, 5))

