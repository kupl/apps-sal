N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A, reverse=True)
judge = sum(A) / (4 * M)
if B[M - 1] < judge:
    print('No')
else:
    print('Yes')
