def gcd(a, b):
    while a:
        (a, b) = (b % a, a)
    return b


(n, a, b, p, q) = map(int, input().split())
ox = n // (a * b // gcd(a, b))
ax = n // a - ox
bx = n // b - ox
print(ax * p + bx * q + ox * max(p, q))
