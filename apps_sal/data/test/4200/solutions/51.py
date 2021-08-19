(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
list.sort(A, reverse=True)
print('Yes') if A[M - 1] >= sum(A) / (4 * M) else print('No')
