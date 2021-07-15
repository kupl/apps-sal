import sys


def fact(k):
    return k ** 2 * (k - 1) ** 2 * (k - 2) ** 2 * (k - 3) ** 2 * (k - 4) ** 2


a, b, c = [int(x) for x in input().split()]

d = b * b - 4 * a * c

x1 = (-b - d ** 0.5) / 2 / a
x2 = (-b + d ** 0.5) / 2 / a

print(max([x1, x2]))
print(min([x1, x2]))

