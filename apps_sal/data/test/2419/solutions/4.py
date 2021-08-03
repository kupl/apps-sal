from math import *
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    x = ceil((-1 + (1 + 8 * (b - a))**0.5) / 2)
    if a % 2 == b % 2:
        while x % 4 not in [0, 3]:
            x += 1
    else:
        while x % 4 not in [1, 2]:
            x += 1
    print(x)
