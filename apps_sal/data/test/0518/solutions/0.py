from math import sin
pi = 3.141592653589793
(n, r) = map(int, input().split())
theta = 2 * pi / n
R = r / (1 - sin(theta / 2))
print(R - r)
