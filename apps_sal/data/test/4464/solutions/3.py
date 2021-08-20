(A, B, C) = map(int, input().split())
if len([A for A in range(A, 10000, A) if A % B == C]):
    print('YES')
else:
    print('NO')
