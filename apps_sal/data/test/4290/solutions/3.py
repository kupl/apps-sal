import math

n, m = list(map(int, input().split()))


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if n >= 2 and m >= 2:
    ans = combinations_count(m, 2) + combinations_count(n, 2)
elif n < 2 and m < 2:
    ans = 0
elif n < 2:
    ans = combinations_count(m, 2)
elif m < 2:
    ans = combinations_count(n, 2)


print(ans)
