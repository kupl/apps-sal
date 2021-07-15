def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

n, a, b, p, q = map(int, input().split())
s = n // a * p + n // b * q - n // lcm(a, b) * min(p, q)
print(s)
