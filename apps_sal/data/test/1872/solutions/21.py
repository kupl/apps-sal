from math import *

pi = 3.141592653589793238462643383279502884197
n, r = list(map(int, input().split()))

a = tan(pi / (2 * n))
b = tan(pi / n)
a = 1 / a + 1 / b
print(r * r / a * n)
