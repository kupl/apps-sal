import math


def takoyaki():
    (N, X, T) = map(int, input().split())
    count = math.ceil(N / X)
    return count * T


result = takoyaki()
print(result)
