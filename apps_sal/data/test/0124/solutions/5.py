(x, y, z) = list(map(int, input().split()))
(a, b, c) = list(map(int, input().split()))
if x > a:
    print('NO')
else:
    a -= x
    if a + b >= y and a + b + c >= y + z:
        print('YES')
    else:
        print('NO')
