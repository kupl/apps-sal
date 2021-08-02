import math
import decimal
output = [
    'x^y^z',  # 0
    'x^z^y',  # 1
    '(x^y)^z',  # 2
    '(x^z)^y',  # 3

    'y^x^z',  # 4
    'y^z^x',  # 5
    '(y^x)^z',  # 6
    '(y^z)^x',  # 7

    'z^x^y',  # 8
    'z^y^x',  # 9
    '(z^x)^y',  # 10
    '(z^y)^x'  # 11
]

x, y, z = map(decimal.Decimal, input().split())


a = [(decimal.Decimal(math.log(x)) * (y**z), 0)]
a += [(decimal.Decimal(math.log(x)) * (z**y), 1)]
a += [(decimal.Decimal(math.log(x)) * y * z, 2)]

a += [(decimal.Decimal(math.log(y)) * (x**z), 4)]
a += [(decimal.Decimal(math.log(y)) * (z**x), 5)]
a += [(decimal.Decimal(math.log(y)) * x * z, 6)]

a += [(decimal.Decimal(math.log(z)) * (x**y), 8)]
a += [(decimal.Decimal(math.log(z)) * (y**x), 9)]
a += [(decimal.Decimal(math.log(z)) * x * y, 10)]

ret = output[0]
# print(a[0][0])
cmp = a[0][0]
for i in range(0, 9):
    if a[i][0] > cmp:
        cmp = a[i][0]
        ret = output[a[i][1]]

print(ret)
