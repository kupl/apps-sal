import fractions
x, y, a, b = map(int, input().split())
nok = x * y // fractions.gcd(x, y)
c = (a // nok) * nok
if c < a:
    c += nok
d = (b // nok) * nok
if d % nok == 0:
    d += nok
print((d - c) // nok)
