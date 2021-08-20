(a, b, x) = map(int, input().split())
if a <= x:
    print('YES' if a + b >= x else 'NO')
else:
    print('NO')
