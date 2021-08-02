import sys
import math
f = sys.stdin


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors[0]


n = int(f.readline().rstrip('\r\n'))
inp = []
gcd = 0
for i in range(n):
    a, b = map(int, f.readline().rstrip('\r\n').split())
    c = a * b
    gcd = math.gcd(gcd, c)
if gcd > 1:
    if gcd <= 10000000000:
        sys.stdout.write(str(prime_factors(gcd)) + "\n")
    else:
        if (math.gcd(gcd, a) > 1):
            sys.stdout.write(str(math.gcd(a, gcd)) + "\n")
        else:
            sys.stdout.write(str(math.gcd(b, gcd)) + '\n')
else:
    sys.stdout.write("-1\n")
