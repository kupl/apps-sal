def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


(n, m, k) = list(map(int, input().split()))
if 2 * n * m % k == 0:
    c = 0
    if k % 2 != 0:
        c = 1
    else:
        k //= 2
    a = n // gcd(k, n)
    k //= gcd(k, n)
    b = m // gcd(m, k)
    if c == 1:
        if a * 2 > n and a * 2 > m:
            b *= 2
        else:
            a *= 2
    if a > n or b > m:
        (a, b) = (b, a)
    print('YES')
    print('0 0')
    print('0', b)
    print(a, '0')
else:
    print('NO')
