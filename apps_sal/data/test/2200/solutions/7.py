import math


def f2(x, a, b):
    t = math.floor(x * a / b)
    r = x % t if t > 0 else x
    #print(x, a, b, r)
    return r


def f(x, a, b):
    r = (x * a) % b
    #print(x, a, b, r)
    return r


n, a, b = list(map(int, input().split(" ")))

x = list(map(int, input().split(" ")))

#r = [f(x[i], a, b) for i in range(len(x))]
r = [int(((x[i] * a) % b) / a) for i in range(len(x))]

print(" ".join(map(str, r)))
