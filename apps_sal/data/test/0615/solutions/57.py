from itertools import accumulate
from bisect import bisect_left
(N, *A) = list(map(int, open(0).read().split()))
A = [0] + list(accumulate(A))
ans = float('inf')
for i in range(2, N - 1):
    lm = A[i] // 2
    l = bisect_left(A, lm)
    if abs(A[l - 1] - lm) < abs(A[l] - lm):
        l -= 1
    rm = (A[i] + A[N]) // 2
    r = bisect_left(A, rm)
    if abs(A[r - 1] - rm) < abs(A[r] - rm):
        r -= 1
    P = A[l]
    Q = A[i] - A[l]
    R = A[r] - A[i]
    S = A[N] - A[r]
    ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
print(ans)
