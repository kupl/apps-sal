import numpy as np


k, q = list(map(int, input().split()))
d = np.array(list(map(int, input().split())), dtype=np.int64)
queries = [tuple(map(int, input().split())) for _ in range(q)]

for n, x, m in queries:
    d_mod = d % m
    rem_d_mod = d_mod[: (n - 1) % k]
    print((n - 1 - (x % m + ((n - 1) // k) * np.sum(d_mod) + np.sum(rem_d_mod)) // m
          - ((n - 1) // k) * np.count_nonzero(d_mod == 0) - np.count_nonzero(rem_d_mod == 0)))

