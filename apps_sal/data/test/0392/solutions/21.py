from math import ceil
from math import sqrt
n = int(input())


def prim(n):
    i = 2
    while i * i <= n:
        if n % (i**2) == 0:
            return i
        i += 1
    return 1


k = n
while k > 1:
    k = prim(n)
    n = n // k


print(n)
