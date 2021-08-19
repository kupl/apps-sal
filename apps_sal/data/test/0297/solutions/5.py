def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


(n, m, k) = list(map(int, input().split()))
if n * m * 2 % k:
    print('NO')
else:
    print('YES')
    g1 = gcd(n, k)
    n //= g1
    k //= g1
    g2 = gcd(m, k)
    m //= g2
    k //= g2
    if k == 1:
        if g1 == 1:
            m *= 2
        else:
            n *= 2
    print('0 0')
    print('0', m)
    print(n, '0')
