from math import sqrt, floor, ceil
n = int(input())
ran = list(range(2, 1 + n // 2))
xx = [d * (n // d - 1) for d in ran]
print(sum(xx) * 4)
