a, b, c = list(map(int, input().split()))
if c == 0:
    if b == a:
        print('YES')
    else:
        print('NO')
elif c > 0:
    if b < a:
        print('NO')
    else:
        if a % c == b % c:
            print('YES')
        else:
            print('NO')
else:
    if b > a:
        print('NO')
    else:
        if a % c == b % c:
            print('YES')
        else:
            print('NO')
