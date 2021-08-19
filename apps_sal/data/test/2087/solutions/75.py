import math
import sys


def nsum(n):
    return n * (n + 1) // 2


a = list(map(int, input().split()))
(a, b, c) = (a[0], a[1], a[2])
num = nsum(a) * nsum(b) * nsum(c)
print(num % 998244353)
