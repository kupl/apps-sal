line = list(map(int, input().split()))
(n, x) = line
encoding = list(map(int, input().split()))
if sum(encoding) + n - 1 == x:
    print('YES')
else:
    print('NO')
