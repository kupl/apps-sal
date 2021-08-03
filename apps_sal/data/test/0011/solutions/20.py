n, a, b, p, q = tuple(map(int, input().split()))

s = (n // a) * p
s += (n // b) * q


def gcd(p, q):
    if p < q:
        return gcd(q, p)
    if q == 0:
        return p
    return gcd(q, p % q)


c = n // ((a * b) // gcd(a, b))
if p < q:
    s -= c * p
else:
    s -= c * q

print(s)
