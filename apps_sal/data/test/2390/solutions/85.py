from itertools import *
N, C, *XV = map(int, open(0).read().split())
X = XV[::2] + [C]
A = [0] + list(accumulate(XV[1::2]))
ans = L = R = 0

for b in range(N + 1):
    T = A[N] - A[b]
    d = C - X[b]
    L = max(L, A[b] - X[b - 1])
    R = max(R, A[b] - 2 * X[b - 1])
    ans = max(ans, L + T - 2 * d, R + T - d)

print(ans)
