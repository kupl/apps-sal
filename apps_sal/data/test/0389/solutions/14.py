from fractions import gcd


def o(n):
    v = 0
    for f in (2, 3, 5):
        while n % f == 0:
            n //= f
            v += 1
    return v if n == 1 else -1


a, b = map(int, input().split())
f = gcd(a, b)
v1, v2 = o(a // f), o(b // f)
print(v1 + v2 if v1 >= 0 and v2 >= 0 else -1)
