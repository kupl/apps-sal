from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 18


A = tuple(accumulate(A, initial=0))
i = 1
j = 3


for mid in range(2, N - 1):
    b = A[i] - A[0]
    c = A[mid] - A[i]
    while i + 1 < mid and abs(b - c) > abs(A[mid] + A[0] - 2 * A[i + 1]):
        i += 1
        b = A[i] - A[0]
        c = A[mid] - A[i]
    j = max(j, mid + 1)
    d = A[j] - A[mid]
    e = A[N] - A[j]
    while j + 1 < N and abs(d - e) > abs(A[N] + A[mid] - 2 * A[j + 1]):
        j += 1
        d = A[j] - A[mid]
        e = A[N] - A[j]

    res = max(b, c, d, e) - min(b, c, d, e)
    ans = min(ans, res)

print(ans)
