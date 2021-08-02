import sys


def fact(n):
    ret = 1
    for x in range(1, n + 1):
        ret = ret * x
    return ret


def C(n, k):
    return fact(n) // (fact(k) * (fact(n - k)))


n = int(input())
print(C(n, 5) * C(n, 5) * 120)
