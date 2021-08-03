from math import factorial
n = int(input())


def c(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


print(c(n + 5 - 1, 5) * c(n + 3 - 1, 3))
