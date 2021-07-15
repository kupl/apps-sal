N = int(input())
A = [int(input()) for _ in range(N)]

M = max(A)
i = A.index(M)
M2 = max(A[:i] + A[i+1:])

for a in A:
    print(M if a != M else M2)
