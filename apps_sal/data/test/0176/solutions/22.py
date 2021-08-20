import math


def ints():
    return list(map(int, input().split()))


def rd():
    return input()


(k, a, b) = ints()
l = a // k if a % k == 0 else a // k + 1
r = b // k
print(int(r - l + 1))
