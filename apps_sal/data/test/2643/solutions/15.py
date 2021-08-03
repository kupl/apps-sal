import numpy as np


k, q = list(map(int, input().split()))
d = np.array(list(map(int, input().split()))).astype(np.int64)
queries = [tuple(map(int, input().split())) for _ in range(q)]

for n, x, m in queries:
    d_mod = d % m
    quotient, rem = divmod(n - 1, k)
    rem_d_mod = d_mod[:rem]
    print((quotient * np.count_nonzero(d_mod) + np.count_nonzero(rem_d_mod) -
          (x % m + quotient * d_mod.sum() + rem_d_mod.sum()) // m))
