import math


def f(n):
    return sum(list(range(n + 1)))


a = int(input())
b = int(input())
middle = (a + b) // 2
dist1 = int(math.fabs(a - middle))
dist2 = int(math.fabs(b - middle))
print(f(dist1) + f(dist2))
