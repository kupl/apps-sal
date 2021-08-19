from math import *
pi = 3.141592653589793
(n, r) = list(map(int, input().split()))
a = tan(pi / (2 * n))
b = tan(pi / n)
a = 1 / a + 1 / b
print(r * r / a * n)
