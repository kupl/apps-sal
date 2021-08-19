(A, B, C) = input().split()
print('YES' if B.startswith(A[-1]) and C.startswith(B[-1]) else 'NO')
