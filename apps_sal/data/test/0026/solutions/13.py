from decimal import *
getcontext().prec = 100
x, y, z = map(Decimal, input().split())

op = ('x^y^z', 'x^z^y', '(x^y)^z', 'y^x^z', 'y^z^x',
      '(y^x)^z', 'z^x^y', 'z^y^x', '(z^x)^y')

arr = [[(y ** z) * x.ln(), 9], [(z ** y) * x.ln(), 8], [(z * y) * x.ln(), 7],
       [(x ** z) * y.ln(), 6], [(z ** x) * y.ln(), 5], [(x * z) * y.ln(), 4],
       [(x ** y) * z.ln(), 3], [(y ** x) * z.ln(), 2], [(x * y) * z.ln(), 1]]

ans = arr[0]
for i in arr:
    if i[0] > ans[0]:
        ans = i

print(op[-ans[1]])
