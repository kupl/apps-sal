from math import gcd
(n, m, q) = list(map(int, input().split()))
kabe = gcd(n, m)
n //= kabe
m //= kabe
for i in range(q):
    (sx, sy, ex, ey) = list(map(int, input().split()))
    sy -= 1
    ey -= 1
    if sx == 1:
        if ex == 1:
            if sy // n == ey // n:
                print('YES')
            else:
                print('NO')
        elif sy // n == ey // m:
            print('YES')
        else:
            print('NO')
    elif ex == 1:
        if sy // m == ey // n:
            print('YES')
        else:
            print('NO')
    elif sy // m == ey // m:
        print('YES')
    else:
        print('NO')
