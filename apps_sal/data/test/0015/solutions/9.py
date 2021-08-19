(a, b, c) = [int(x) for x in input().split()]
if c == 0:
    if b != a:
        print('NO')
    else:
        print('YES')
else:
    if c < 0:
        c = -c
        d = a
        a = b
        b = d
    if b >= a and (b - a) % c == 0:
        print('YES')
    else:
        print('NO')
