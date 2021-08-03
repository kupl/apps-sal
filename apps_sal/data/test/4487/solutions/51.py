A, B, C = open(0).read().split()
print('YES' if (A[len(A) - 1] == B[0]) and (B[len(B) - 1] == C[0]) else 'NO')
