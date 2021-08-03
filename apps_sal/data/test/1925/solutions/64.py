import math


def f(A, B, x):
    return math.floor(A * x / B) - A * math.floor(x / B)


def main(A, B, N):
    if N < B:
        return f(A, B, N)
    else:
        return f(A, B, B - 1)


A, B, N = list(map(int, input().split()))
print((main(A, B, N)))
