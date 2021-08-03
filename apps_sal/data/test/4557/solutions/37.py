a, b, x = map(int, input().split())

if a > x:
    print('NO')
else:
    if x - a <= b:
        print('YES')
    else:
        print('NO')
