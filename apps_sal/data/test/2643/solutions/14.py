import numpy as np

k, q = map(int, input().split())
d = np.array(input().split(), dtype=np.int)
for _ in range(q):
    n, x, m = map(int, input().split())
    quot = (n - 1) // k
    rest = (n - 1) % k
    dmod = d % m
    same = (k - np.count_nonzero(dmod)) * quot + rest - np.count_nonzero(dmod[:rest])
    a_last = x % m + dmod.sum() * quot + dmod[:rest].sum()
    beyond = a_last // m
    print(n - 1 - same - beyond)
