[N, M] = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
A = sorted(A, reverse=True)
if A[M - 1] < sum(A) * 1 / (4 * M):
    print('No')
else:
    print('Yes')
