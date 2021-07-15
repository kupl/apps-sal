n = int(input())
from math import factorial
print(factorial(2*(n-1)) // factorial(n-1) // factorial(n-1))
