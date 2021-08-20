(A, B, C) = map(int, input().split())
check = False
for i in range(1, B + 1):
    if A * i % B == C:
        check = True
print('YES' if check else 'NO')
