from fractions import gcd
(x, y, a, b) = map(int, input().split())
nok = x * y // gcd(x, y)
xx = a // nok * nok
if a % nok != 0:
    xx += nok
yy = b // nok * nok
if xx > b:
    print(0)
else:
    if yy % nok == 0:
        f = 1
    else:
        f = 0
    print((yy - xx) // nok + f)
