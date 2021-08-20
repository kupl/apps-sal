(A, B, X) = map(int, input().split())
if X >= A and B >= X - A:
    print('YES')
else:
    print('NO')
