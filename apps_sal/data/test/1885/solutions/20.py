import sys


def c5(n):
    return n * (n - 1) * (n - 2) * (n - 3) * (n - 4) // 2 // 3 // 4 // 5


def c6(n):
    return c5(n) * (n - 5) // 6


def c7(n):
    return c6(n) * (n - 6) // 7


n = int(input())

print(c5(n) + c6(n) + c7(n))
