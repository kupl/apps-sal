import math
n, m = map(int, input().split())


def combinations_count(a, b):
    if a != 0 and a != 1:
        return math.factorial(a) // (math.factorial(a - b) * math.factorial(b))
    else:
        return 0


print(combinations_count(n, 2) + combinations_count(m, 2))
