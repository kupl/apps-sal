(A, B, C) = list(map(int, input().split()))
s = 0
for i in range(1, B + 1):
    x = A * i % B
    if x == C:
        s = s + 1
    else:
        s = s
if s != 0:
    print('YES')
else:
    print('NO')
