from math import sin, pi
n, r = map(int, input().split())
R = (r * sin(pi / n)) / (1 - sin(pi / n))
print(R)
