from decimal import Decimal
x,y,z = map(Decimal, input().split())
a = ['x^y^z', 'x^z^y', '(x^y)^z', 'y^x^z', 'y^z^x', '(y^x)^z',
         'z^x^y', 'z^y^x', '(z^x)^y']
f = [y ** z * x.ln(), z ** y * x.ln(), y * z * x.ln(), x ** z * y.ln(),
       z ** x * y.ln(), x * z * y.ln(), x ** y * z.ln(), y ** x * z.ln(),
       x * y * z.ln()]
max, res = -10**18, 0
for i, j in enumerate(f):
    if j > max:
        max, res = j, i
print(a[res])
