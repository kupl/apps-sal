import math
import re


def f(n):
    if n - math.floor(n) < 0.5:
        return n
    else:
        return math.ceil(n)


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

n1 = n
s = sum(a)
sred = s / n
while f(sred) != k:
    s += k
    n += 1
    sred = s / n

print(n - n1)
