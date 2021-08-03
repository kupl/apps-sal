N, M = map(int, input().split())

A = list(map(int, input().split()))

sums = sum(A)

A.sort(reverse=True)


if 4 * M * A[M - 1] >= sums:
    print('Yes')
else:
    print('No')
