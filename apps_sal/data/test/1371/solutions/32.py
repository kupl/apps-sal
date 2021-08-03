import math


def H(n, r):
    return math.factorial(n + r - 1) // (math.factorial(n - 1) * math.factorial(r))


S = int(input())
s = 0
i = 1
while S // i > 2:
    s += H(i, S - 3 * i)
    i += 1
print(s % (10**9 + 7))
