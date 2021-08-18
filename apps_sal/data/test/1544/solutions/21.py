import math


def choose(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


n = int(input())

f = math.factorial

result = choose(n - 1 + 5, 5) * choose(n - 1 + 3, 3)


print(result)
