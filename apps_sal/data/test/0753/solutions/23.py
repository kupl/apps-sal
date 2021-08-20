def gcd(a, b):
    c = a % b
    return gcd(b, c) if c else b


(a, b, c, d) = map(int, input().split())
if a * d < b * c:
    (a, b, c, d) = (b, a, d, c)
p = a * d - b * c
q = d * a
t = gcd(p, q)
print(str(p // t) + '/' + str(q // t))
