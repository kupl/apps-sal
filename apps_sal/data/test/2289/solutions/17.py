(n, q) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
K = [int(i) for i in input().split()]
A = a[:]
for i in range(1, n):
    A[i] += A[i - 1]


def bs(A, key):
    (lo, hi) = (0, len(A) - 1)
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            hi = mid - 1
        elif A[mid] < key:
            lo = mid + 1
    return hi


D = 0
for i in range(q):
    D += K[i]
    j = bs(A, D)
    if j == n - 1:
        D = 0
        j = -1
    print(n - (j + 1))
