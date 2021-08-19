import bisect
(n, *A) = map(int, open(0).read().split())
A.sort()
m = A[-1]
i = bisect.bisect_right(A, m / 2)
print(m, [A[i - 1], A[i]][abs(A[i - 1] - m / 2) > abs(A[i] - m / 2)])
