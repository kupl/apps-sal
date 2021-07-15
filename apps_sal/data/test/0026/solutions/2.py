import math
from decimal import *
getcontext().prec = 1024
x, y, z = list(map(Decimal, input().split(" ")))
l = lambda t: Decimal(math.log(t))
a = [
	(lambda: y ** z * l(x), "x^y^z"),
	(lambda: z ** y * l(x), "x^z^y"),
	(lambda: y * z * l(x), "(x^y)^z"),

	(lambda: x ** z * l(y), "y^x^z"),
	(lambda: z ** x * l(y), "y^z^x"),
	(lambda: x * z * l(y), "(y^x)^z"),

	(lambda: x ** y * l(z), "z^x^y"),
	(lambda: y ** x * l(z), "z^y^x"),
	(lambda: x * y * l(z), "(z^x)^y"),
]
m = -1
ans = ""
for calc, exp in a:
	q = calc()
	if q > m:
		m = q
		ans = exp
print(ans)

