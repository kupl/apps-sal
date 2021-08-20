from fractions import Decimal, Fraction
(a, b) = input().split()
a = Fraction(a)
x = Decimal(b).as_integer_ratio()
b = Fraction(x[0], x[1])
print(int(a * b))
