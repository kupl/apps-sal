n, a, b, p, q = map(int ,input().split())

red_max = n // a
blue_max = n // b

import fractions

gcd = (a*b) // fractions.math.gcd(a, b)
commons = n // gcd

if p > q:
    print(red_max*p + (blue_max-commons)*q)
else:
    print((red_max-commons)*p + blue_max*q)
