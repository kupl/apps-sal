A, B, C = input().split(" ")

if A[len(A) - 1] == B[0] and B[len(B) - 1] == C[0]:
    print('YES')
else:
    print('NO')
