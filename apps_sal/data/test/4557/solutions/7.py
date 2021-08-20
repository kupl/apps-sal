(a, b, c) = map(int, input().split())
if c < a:
    print('NO')
elif c > a + b:
    print('NO')
else:
    print('YES')
