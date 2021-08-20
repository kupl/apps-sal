EPS = 1e-11
INF = float('inf')


def multiply(a, b):
    m = INF
    M = -INF
    for i in range(2):
        for j in range(2):
            m = min(m, a[i] * b[j])
            M = max(M, a[i] * b[j])
    return (m, M)


def intersect(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


(a, b) = list(map(float, input().split()))
(c, d) = list(map(float, input().split()))
lo = 0
hi = 1000000000.0
nIters = 0
while nIters < 1000 and abs(lo - hi) > EPS:
    mi = (lo + hi) / 2
    i1 = multiply((a - mi, a + mi), (d - mi, d + mi))
    i2 = multiply((b - mi, b + mi), (c - mi, c + mi))
    if intersect(i1, i2):
        hi = mi
    else:
        lo = mi
    nIters += 1
print('{:.10f}'.format(hi))
