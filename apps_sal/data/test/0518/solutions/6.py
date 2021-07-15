from math import sin, pi

n, r = list(map(int, input().split()))

print(r * sin(pi / n) / (1 - sin(pi / n)))

