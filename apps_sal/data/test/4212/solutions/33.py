import itertools
from operator import mul
from functools import reduce


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, list(range(n, n - r, -1)), 1)
    denom = reduce(mul, list(range(1, r + 1)), 1)
    return numer // denom


(N, M, Q) = list(map(int, input().split()))
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    (a[i], b[i], c[i], d[i]) = list(map(int, input().split()))
l = list(range(1, M + 1))
h = combinations_count(M + N - 1, N)
H = [0] * h
i = 0
for v in itertools.combinations_with_replacement(l, N):
    H[i] = v
    i += 1
D = [0 for j in range(h)]
for i in range(h):
    for j in range(Q):
        if H[i][b[j] - 1] - H[i][a[j] - 1] == c[j]:
            D[i] += d[j]
print(max(D))
