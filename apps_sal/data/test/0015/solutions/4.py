a, b, c = list(map(int, input().split()))
if c == 0:
    if b == a:
        print('YES')
    else:
        print('NO')
else:
    if (b - a) % c == 0 and (b - a) // c >= 0:
        print('YES')
    else:
        print('NO')
