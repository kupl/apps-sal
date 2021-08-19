from math import factorial
(a, b) = list(map(int, input().split()))
print(factorial(min(a, b)))
