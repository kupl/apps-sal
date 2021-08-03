import math


def c(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def p(n, r):
    if n < r:
        return 0
    return math.factorial(n) // math.factorial(n - r)


def h(n, r):
    return c(n + r - 1, r)


s = int(input())
n = math.floor(s / 3)
out = 0
for i in range(n):
    out += h(i + 1, s - (i + 1) * 3)
print(out % 1000000007)
