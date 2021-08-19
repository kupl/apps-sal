from math import factorial
n = int(input())
kek = factorial(n) // factorial(n // 2) // factorial(n // 2) // 2
print(kek * factorial(n // 2) * factorial(n // 2) // (n // 2) // (n // 2))
