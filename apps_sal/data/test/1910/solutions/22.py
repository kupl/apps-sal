import math


def choose(n, r):
    return math.factorial(n) // math.factorial(n - r) // math.factorial(r)


def choose2(n, r):
    return math.factorial(n) // math.factorial(n - r)


n = int(input())
result = int(4 * ((n - 3) * 3 ** 2 * 4 ** (n - 4) + 2 * 3 * 4 ** (n - 3)))
print(result)
