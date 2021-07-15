from fractions import Fraction

x, y, n = input().split()
x = int(x)
y = int(y)
n = int(n)
if (2 * Fraction(x, y) - Fraction(x / y).limit_denominator(n)).denominator >= Fraction(x/y).limit_denominator(n).denominator:
    b=Fraction(x / y).limit_denominator(n)
    print(str(b.numerator)+"/"+str(b.denominator))
else:
    a= 2 * Fraction(x, y) - Fraction(x / y).limit_denominator(n)
    print(str(a.numerator)+"/"+str(a.denominator))


