3


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


(n, a, b, p, q) = list(map(int, input().split()))
s = n // a * p + n // b * q
s -= n // (a * b // gcd(a, b)) * min(p, q)
print(s)
