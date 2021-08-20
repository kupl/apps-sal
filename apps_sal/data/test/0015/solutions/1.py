(a, b, c) = list(map(int, input().split()))
if c != 0:
    if c * (b - a) >= 0 and (b - a) % c == 0:
        print('YES')
    else:
        print('NO')
elif b == a:
    print('YES')
else:
    print('NO')
