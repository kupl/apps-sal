import math
x = int(input())
t = math.ceil(x / 5.5)


def f(n):
    return 6 * n - n // 2


if x <= f(t - 1):
    print(t - 1)
elif x <= f(t):
    print(t)
else:
    print(t + 1)
