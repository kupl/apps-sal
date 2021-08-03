import math
import fractions
a, b = list(map(str, input().split()))
a, b = int(a), fractions.Fraction(b)
print((math.floor(a * b)))
