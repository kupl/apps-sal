(A, B, C) = map(str, input().split())
A_num = len(A)
B_num = len(B)
if A[A_num - 1] == B[0] and B[B_num - 1] == C[0]:
    print('YES')
else:
    print('NO')
