import math


def L():
    return list(map(int, input().split()))


[n, k] = L()
print(math.floor(math.log(n, k)) + 1)
