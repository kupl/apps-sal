N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
S = sum(A)
if A[M - 1] >= S / (4 * M):
    print("Yes")
else:
    print("No")
