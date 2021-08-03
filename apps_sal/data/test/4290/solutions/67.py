import math

n, m = list(map(int, input().split()))


def c(a, b):
    if a >= 2:
        return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))
    else:
        return 0


print((c(n, 2) + c(m, 2)))
