N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort(reverse=True)
num = sum(A)

if A[M - 1] >= num / (4 * M):
    print("Yes")
else:
    print("No")
