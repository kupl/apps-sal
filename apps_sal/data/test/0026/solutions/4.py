from decimal import *
getcontext().prec = 500
x, y, z = map(float, input().split())
x = Decimal(x)
y = Decimal(y)
z = Decimal(z)
a = [Decimal(0) for i in range(12)]
a[0] = ((Decimal(x).log10()) * Decimal(Decimal(y) ** Decimal(z)))
a[1] = ((Decimal(x).log10()) * Decimal(Decimal(z) ** Decimal(y)))
a[2] = ((Decimal(x).log10()) * Decimal(Decimal(y) * Decimal(z)))
a[3] = ((Decimal(x).log10()) * Decimal(Decimal(y) * Decimal(z)))
a[4] = ((Decimal(y).log10()) * Decimal(Decimal(x) ** Decimal(z)))
a[5] = ((Decimal(y).log10()) * Decimal(Decimal(z) ** Decimal(x)))
a[6] = ((Decimal(y).log10()) * Decimal(Decimal(x) * Decimal(z)))
a[7] = ((Decimal(y).log10()) * Decimal(Decimal(x) * Decimal(z)))
a[8] = ((Decimal(z).log10()) * Decimal(Decimal(x) ** Decimal(y)))
a[9] = ((Decimal(z).log10()) * Decimal(Decimal(y) ** Decimal(x)))
a[10] = ((Decimal(z).log10()) * Decimal(Decimal(x) * Decimal(y)))
a[11] = ((Decimal(z).log10()) * Decimal(Decimal(x) * Decimal(y)))
maxx = a[0]
for i in range(12):
    if a[i] > maxx:
        maxx = a[i]
s = ["" for i in range(12)]
s[0] = "x^y^z"
s[1] = "x^z^y"
s[2] = "(x^y)^z"
s[3] = "(x^z)^y"
s[4] = "y^x^z"
s[5] = "y^z^x"
s[6] = "(y^x)^z"
s[7] = "(y^z)^x"
s[8] = "z^x^y"
s[9] = "z^y^x"
s[10] = "(z^x)^y"
s[11] = "(z^y)^x"
for i in range(12):
    if a[i] == maxx:
        print(s[i])
        break
