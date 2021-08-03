import math
from decimal import *
p, q, r = x, y, z = input().split()
x = float(x)
y = float(y)
z = float(z)
if(x > 1 and y > 1 and z > 1):
    p = z * math.log(y) + math.log(math.log(x))
    ans = "x^y^z"
    max = p
    p = y * math.log(z) + math.log(math.log(x))
    if(p > max):
        max = p
        ans = "x^z^y"
    p = math.log(y) + math.log(z) + math.log(math.log(x))
    if(p > max):
        max = p
        ans = "(x^y)^z"
    p = z * math.log(x) + math.log(math.log(y))
    if(p > max):
        max = p
        ans = "y^x^z"
    p = x * math.log(z) + math.log(math.log(y))
    if(p > max):
        max = p
        ans = "y^z^x"
    p = math.log(x) + math.log(z) + math.log(math.log(y))
    if(p > max):
        max = p
        ans = "(y^x)^z"
    p = y * math.log(x) + math.log(math.log(z))
    if(p > max):
        max = p
        ans = "z^x^y"
    p = x * math.log(y) + math.log(math.log(z))
    if(p > max):
        max = p
        ans = "z^y^x"
    p = math.log(x) + math.log(y) + math.log(math.log(z))
    if(p > max):
        max = p
        ans = "(z^x)^y"
else:
    if(not(x < 1 and y < 1 and z < 1)):
        x = Decimal(p)
        y = Decimal(q)
        z = Decimal(r)
    p = x**(y**z)
    max = p
    ans = "x^y^z"
    p = x**(z**y)
    if(p > max):
        max = p
        ans = "x^z^y"
    p = x**(y * z)
    if(p > max):
        max = p
        ans = "(x^y)^z"
    p = y**(x**z)
    if(p > max):
        max = p
        ans = "y^x^z"
    p = y**(z**x)
    if(p > max):
        max = p
        ans = "y^z^x"
    p = y**(x * z)
    if(p > max):
        max = p
        ans = "(y^x)^z"
    p = z**(x**y)
    if(p > max):
        max = p
        ans = "z^x^y"
    p = z**(y**x)
    if(p > max):
        max = p
        ans = "z^y^x"
    p = z**(x * y)
    if(p > max):
        max = p
        ans = "(z^x)^y"
print(ans)
