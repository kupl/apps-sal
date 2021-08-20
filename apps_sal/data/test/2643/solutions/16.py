import numpy as np
(k, q) = list(map(int, input().split()))
d = np.array(input().split(), np.int64)
nxm = [list(map(int, input().split())) for _ in range(q)]
for (n, x, m) in nxm:
    dd = d % m
    ans = n - 1
    (divq, divr) = divmod(n - 1, k)
    dd_r = dd[:divr]
    ans -= (k - np.count_nonzero(dd)) * divq
    ans -= divr - np.count_nonzero(dd_r)
    last = x + np.sum(dd) * divq + np.sum(dd_r)
    ans -= last // m - x // m
    print(ans)
