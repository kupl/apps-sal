from math import sin
(n, r) = [int(i) for i in input().split()]
pi = 3.14159265359
print(r / (2 * sin(pi * (1 / 2 - 1 / n)) / sin(2 * pi / n) - 1))
