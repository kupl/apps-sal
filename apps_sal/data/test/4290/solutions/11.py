import math


def combinations_count(n, r):
    if n < 2:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


(n, m) = [int(i) for i in input().split()]
print(combinations_count(n, 2) + combinations_count(m, 2))
