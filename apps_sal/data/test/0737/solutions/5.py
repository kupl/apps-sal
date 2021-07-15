from math import floor, ceil, sqrt

n = int(input())

a = floor(sqrt(n))
b = ceil(sqrt(n))

if n == a * a: print(4 * a)
elif n <= a * b: print(2 * (a + b))
else: print(4 * b)

