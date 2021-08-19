import math

s = ['x^y^z',
     'x^z^y',
     '(x^y)^z',
     '(x^z)^y',
     'y^x^z',
     'y^z^x',
     '(y^x)^z',
     '(y^z)^x',
     'z^x^y',
     'z^y^x',
     '(z^x)^y',
     '(z^y)^x']

x, y, z = map(float, input().split())

ma = float('-inf')
c = -1

if x > 1:
    if ma < z * math.log(y) + math.log(math.log(x)):
        ma = z * math.log(y) + math.log(math.log(x))
        c = 0

    if ma < y * math.log(z) + math.log(math.log(x)):
        ma = y * math.log(z) + math.log(math.log(x))
        c = 1

    if ma < math.log(y) + math.log(z) + math.log(math.log(x)):
        ma = math.log(y) + math.log(z) + math.log(math.log(x))
        c = 2

if y > 1:
    if ma < z * math.log(x) + math.log(math.log(y)):
        ma = z * math.log(x) + math.log(math.log(y))
        c = 4

    if ma < x * math.log(z) + math.log(math.log(y)):
        ma = x * math.log(z) + math.log(math.log(y))
        c = 5

    if ma < math.log(x) + math.log(z) + math.log(math.log(y)):
        ma = math.log(x) + math.log(z) + math.log(math.log(y))
        c = 6

if z > 1:
    if ma < y * math.log(x) + math.log(math.log(z)):
        ma = y * math.log(x) + math.log(math.log(z))
        c = 8

    if ma < x * math.log(y) + math.log(math.log(z)):
        ma = x * math.log(y) + math.log(math.log(z))
        c = 9

    if ma < math.log(x) + math.log(y) + math.log(math.log(z)):
        ma = math.log(x) + math.log(y) + math.log(math.log(z))
        c = 10

# if max(x , y, z) <= 1
if c == -1:
    if ma < x ** (y ** z):
        ma = x ** (y ** z)
        c = 0

    if ma < x ** (z ** y):
        ma = x ** (z ** y)
        c = 1

    if ma < (x ** y) ** z:
        ma = (x ** y) ** z
        c = 2

    if ma < y ** (x ** z):
        ma = y ** (x ** z)
        c = 4

    if ma < y ** (z ** x):
        ma = y ** (z ** x)
        c = 5

    if ma < (y ** x) ** z:
        ma = (y ** x) ** z
        c = 6

    if ma < z ** (x ** y):
        ma = z ** (x ** y)
        c = 8

    if ma < z ** (y ** x):
        ma = z ** (y ** x)
        c = 9

    if ma < (z ** x) ** y:
        ma = (z ** x) ** y
        c = 10

print(s[c])
