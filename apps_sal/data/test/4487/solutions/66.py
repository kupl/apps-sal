A, B, C = input().split()
if A[len(A)-1:len(A)] == B[0:1] and B[len(B)-1:len(B)] == C[0:1]:
    print('YES')
else:
    print('NO')

