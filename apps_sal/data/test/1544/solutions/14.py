n=int(input())
from math import factorial
def c(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)
print(c(n+5-1,5) * c(n+3-1,3))

