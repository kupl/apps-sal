import math
(A, B, C) = map(int, input().split())
for i in range(1, B + 1):
    if A * i % B == C:
        print('YES')
        break
else:
    print('NO')
