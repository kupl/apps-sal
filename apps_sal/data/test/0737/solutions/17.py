from math import *
n = int(input())
x = n**0.5
if x == ceil(x):
    print("%d" % (4 * x))
else:
    x = ceil(x)
    y = n // x
    if n != x * y:
        y += 1
    print("%d" % (2 * (x + y)))
