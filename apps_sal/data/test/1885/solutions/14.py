from math import factorial


def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


n = int(input())
print(C(n, 5) + C(n, 6) + C(n, 7))
