import sys
(n, k) = map(int, input().split())
z = n // k
if z % 2 == 1:
    print('YES')
else:
    print('NO')
