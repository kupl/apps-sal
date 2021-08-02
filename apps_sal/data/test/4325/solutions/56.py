import math


def cin():
    return list(map(int, input().split()))


A = cin()
N = A[0]
X = A[1]
T = A[2]


print((math.ceil(N / X) * T))
