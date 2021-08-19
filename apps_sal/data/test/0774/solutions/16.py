from fractions import Fraction
(x, y, n) = input().split()
x = int(x)
y = int(y)
n = int(n)
if Fraction(x / y).limit_denominator(n) == 0:
    print('0/1')
elif Fraction(x / y).limit_denominator(n) == int(Fraction(x, y).limit_denominator(n)):
    print(str(Fraction(x, y).limit_denominator(n)) + '/1')
elif (2 * Fraction(x, y) - Fraction(x / y).limit_denominator(n)).denominator >= Fraction(x / y).limit_denominator(n).denominator:
    print(Fraction(x / y).limit_denominator(n))
else:
    a = 2 * Fraction(x, y) - Fraction(x / y).limit_denominator(n)
    print(str(a.numerator) + '/' + str(a.denominator))
