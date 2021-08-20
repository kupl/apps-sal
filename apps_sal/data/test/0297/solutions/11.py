import math
(n, m, k) = [int(x) for x in input().split()]
if 2 * n * m % k != 0:
    print('NO')
else:
    if k % 2 == 0:
        k //= 2
        g = math.gcd(k, n)
        k1 = k // g
        a = n // g
        b = m // k1
    else:
        g = math.gcd(k, n)
        a = n // g
        k1 = k // g
        b = m // k1
        if a < n:
            a *= 2
        else:
            b *= 2
    print('YES')
    print(0, 0)
    print(a, 0)
    print(0, b)
