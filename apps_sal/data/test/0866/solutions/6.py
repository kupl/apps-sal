import numpy as np
x, y = list(map(int, input().split()))

def comb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return g1[n]*g2[r]*g2[n-r]%mod

if (x+y)%3 != 0:
    print((0))
else:
    mod, N = 10**9+7, 10**6
    g1, g2, inverse = [1, 1], [1, 1], [0, 1]
    for i in range(2, N+1):
        g1.append((g1[-1]*i)%mod)
        inverse.append((-inverse[mod%i]*(mod//i))%mod)
        g2.append((g2[-1]*inverse[-1])%mod)
    a = np.array([[1, 2], [2, 1]])
    b = np.array([x, y])
    x0, y0 = np.linalg.solve(a, b)
    print((comb(int(x0+y0), int(x0), mod)))

