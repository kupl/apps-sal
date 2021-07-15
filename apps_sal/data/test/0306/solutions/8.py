import sys

def calc(a, b, p, x):
    ans = 0
    power = pow(a, p - 2, p)
    a2, b2, s, d1 = 1, b, 0, -b
    prod = p * (p - 1)
    while s < p - 1:
        k = (d1 + s) % p
        L = x - s - (p - 1) * k
        ans += L // prod + 1
        d1 = (d1 * power) % p
        s += 1
    return str(ans)
 
 
a, b, p, x = list(map(int,sys.stdin.readline().split()))
sys.stdout.write(calc(a, b, p, x))


