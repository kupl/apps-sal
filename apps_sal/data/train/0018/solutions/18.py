from math import cos, sin, pi
t = int(input())
for test in range(t):
    n = int(input())
    if n == 2:
        print(1.)
    else:
        print(sin(pi / n) / (1 - cos(pi / n)))
