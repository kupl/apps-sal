import math


def f2(x, a, b):
    t = math.floor(x * a / b)
    r = x % t if t > 0 else x
    return r


def f(x, a, b):
    r = x * a % b
    return r


(n, a, b) = list(map(int, input().split(' ')))
x = list(map(int, input().split(' ')))
r = [int(x[i] * a % b / a) for i in range(len(x))]
print(' '.join(map(str, r)))
