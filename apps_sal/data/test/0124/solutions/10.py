(x, y, z) = map(int, input().split())
(a, b, c) = map(int, input().split())
if a >= x:
    if a + b - y - x >= 0:
        if a + b + c - x - y - z >= 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
