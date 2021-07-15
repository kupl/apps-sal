from math import log
from decimal import Decimal

def a1(x, y, z):
    return (y ** z) * Decimal(log(x))

def s1(x, y, z):
    return "x^y^z"

def a2(x, y, z):
    return (z ** y) * Decimal(log(x))

def s2(x, y, z):
    return "x^z^y"

def a3(x, y, z):
    return (y * z) * Decimal(log(x))

def s3(x, y, z):
    return "(x^y)^z"

def a4(x, y, z):
    return (y * z) * Decimal(log(x))

def s4(x, y, z):
    return "(x^z)^y"

def a5(x, y, z):
    return (x ** z) * Decimal(log(y))

def s5(x, y, z):
    return "y^x^z"

def a6(x, y, z):
    return (z ** x) * Decimal(log(y))

def s6(x, y, z):
    return "y^z^x"

def a7(x, y, z):
    return (x * z) * Decimal(log(y))

def s7(x, y, z):
    return "(y^x)^z"

def a8(x, y, z):
    return (z * x) * Decimal(log(y))

def s8(x, y, z):
    return "(y^z)^x"

def a9(x, y, z):
    return (x ** y) * Decimal(log(z))

def s9(x, y, z):
    return "z^x^y"

def a10(x, y, z):
    return (y ** x) * Decimal(log(z))

def s10(x, y, z):
    return "z^y^x"

def a11(x, y, z):
    return (x * y) * Decimal(log(z))

def s11(x, y, z):
    return "(z^x)^y"

def a12(x, y, z):
    return (y * x) * Decimal(log(z))

def s12(x, y, z):
    return "(z^y)^x"

x, y, z = list(map(Decimal, input().split()))
ans = s1(x, y, z)
a = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
max = a1(x, y, z)
for i in range (12):
    if max < a[i](x, y, z):
        ans = s[i](x, y, z)
        max = a[i](x, y, z)
print(ans)

