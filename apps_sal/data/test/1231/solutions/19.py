(a, b) = map(int, input().split())
if a > b + 1:
    print('NO')
elif a == b == 0:
    print('NO')
elif b > a + 1:
    print('NO')
else:
    print('YES')
