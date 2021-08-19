from fractions import gcd
try:
    while True:
        (n, a, b, p, q) = list(map(int, input().split()))
        print(n // a * p + n // b * q - n // (a // gcd(a, b) * b) * min(p, q))
except EOFError:
    pass
