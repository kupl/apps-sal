(a, b, c) = list(map(int, input().split()))
(g, q, y) = list(map(int, input().split()))
g -= a
if g >= 0:
    q -= b - g
    if q >= 0:
        y -= c - q
        if y >= 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
