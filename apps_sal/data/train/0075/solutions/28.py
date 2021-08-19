from math import sin, pi
t = int(input())
while t != 0:
    t -= 1
    n = int(input())
    k = 1 / sin(pi / (4 * n))
    print(k / 2)
