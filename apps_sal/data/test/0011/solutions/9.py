def gcd(a, b):
    while (a % b != 0):
        c = a % b
        a = b
        b = c
    return b


n, a, b, p, q = map(int, input().split())
if (p > q):
    c1 = p
    p = q
    q = c1
    c = a
    a = b
    b = c
t = (a // gcd(a, b)) * b
print(int((n // a) * p + (n // b) * q - (n // t) * p))
