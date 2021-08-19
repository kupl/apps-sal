from numpy import int64, count_nonzero
(K, Q, *I) = map(int, open(0).read().split())
(D, NXM) = (int64(I[:K]), I[K:])
for (n, x, m) in zip(*[iter(NXM)] * 3):
    (q, r) = divmod(n - 1, K)
    T = D % m
    a = (K - count_nonzero(T)) * q + r - count_nonzero(T[:r])
    b = (x % m + T.sum() * q + T[:r].sum()) // m
    print(n - 1 - a - b)
