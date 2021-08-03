A, B, K = map(int, input().split())
C = A
if K >= B - A:
    for f in range(1 + B - A):
        print(C)
        C += 1
else:
    B -= (K - 1)
    for i in range(K):
        print(A)
        A += 1
        if A == B:
            break
    for j in range(K):
        print(B)
        B += 1
