def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(m // a, '/', n // a, sep='')


(a, b, c, d) = map(int, input().split())
m = 1
n = 1
if a == b:
    if c == d:
        print(0, '/', 1, sep='')
    elif c > d:
        m = b * c - a * d
        n = c * b
        gcd(m, n)
    else:
        m = a * d - c * b
        n = a * d
        gcd(m, n)
elif c / d == a / b:
    print(0, '/', 1)
elif c / d > a / b:
    m = b * c - a * d
    n = c * b
    gcd(m, n)
else:
    m = a * d - c * b
    n = a * d
    gcd(m, n)
