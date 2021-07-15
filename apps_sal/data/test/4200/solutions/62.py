N, M = list(map(int, input().split()))
A = sorted([int(x) for x in input().split()], reverse=True)
sumA = sum(A)

if A[M - 1] >= sumA / (4 * M):
    print("Yes")
else:
    print('No')

