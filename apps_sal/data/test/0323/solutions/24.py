from math import factorial

A, B = input().split()
A, B = int(A), int(B)
print(factorial(min(A, B)))
