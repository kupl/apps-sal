(n, k) = list(map(int, input().split()))
A = [i for i in range(0, 2 * n + 1)]
for i in range(1, k + 1):
    (A[2 * i], A[2 * i - 1]) = (A[2 * i - 1], A[2 * i])
print(' '.join(map(str, A[1:])))
