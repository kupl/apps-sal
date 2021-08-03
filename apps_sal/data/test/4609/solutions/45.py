N = int(input())
A = dict()
for _ in range(N):
    a = int(input())
    if a not in A:
        A[a] = 0
    A[a] = 1 - A[a]
print((sum(A.values())))
