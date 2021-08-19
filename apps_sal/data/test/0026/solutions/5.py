from decimal import *
getcontext().prec = 333
(a, b, c) = input().split()
x = Decimal(a)
y = Decimal(b)
z = Decimal(c)
l = [x.ln() * y ** z, x.ln() * z ** y, (x ** y).ln() * z, (x ** z).ln() * y, y.ln() * x ** z, y.ln() * z ** x, (y ** x).ln() * z, (y ** z).ln() * x, z.ln() * x ** y, z.ln() * y ** x, (z ** x).ln() * y, (z ** y).ln() * x]
m = max(l)
s = ['x^y^z', 'x^z^y', '(x^y)^z', '(x^z)^y', 'y^x^z', 'y^z^x', '(y^x)^z', '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
i = 0
for j in range(12):
    if abs(l[j] - m) < Decimal('.' + '0' * 100 + '1'):
        i = j
        break
print(s[i])
