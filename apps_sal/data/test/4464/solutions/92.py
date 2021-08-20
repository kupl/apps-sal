(A, B, C) = map(int, input().split(' '))
candidate = [A * i % B for i in range(1, B - 1)]
if C in candidate:
    print('YES')
else:
    print('NO')
