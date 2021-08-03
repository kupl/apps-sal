from math import cos, pi, sin

for _ in range(int(input())):
    n = int(input())
    alpha = pi / (n * 2)
    print(cos(alpha) / sin(alpha))
