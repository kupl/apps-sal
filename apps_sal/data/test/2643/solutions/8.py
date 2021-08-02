import numpy as np
k, q = list(map(int, input().split()))
d = np.array(list(map(int, input().split())))
for _ in range(q):
    n, x, m = list(map(int, input().split()))
    dm = d % m
    a = (n - 1) % k
    ans = n - 1
    ans -= np.count_nonzero(dm[:a] == 0) * ((n - 1) // k + 1)
    ans -= np.count_nonzero(dm[a:] == 0) * ((n - 1) // k)
    ans -= (x % m + np.sum(dm[:a]) * ((n - 1) // k + 1) + np.sum(dm[a:]) * ((n - 1) // k)) // m
    print(ans)
