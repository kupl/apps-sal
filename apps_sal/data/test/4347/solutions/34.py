from math import factorial
n = int(input())
ans = factorial(n // 2 - 1) ** 2
ans *= factorial(n) // factorial(n // 2) ** 2 // 2
print(ans)
