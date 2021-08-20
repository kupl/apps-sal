def gcd(a, b):
    if b < 1:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a % b)


(n, a, b, p, q) = list(map(int, input().split()))
l = [n // a, n // b, n // (a * b // gcd(a, b))]
print((l[0] - l[2]) * p + (l[1] - l[2]) * q + l[2] * max(p, q))
