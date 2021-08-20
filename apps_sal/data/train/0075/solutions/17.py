from math import cos, pi, sin, sqrt
for _ in range(int(input())):
    n = int(input())
    k0 = (n + 2) // 4
    alpha = k0 * pi / n
    print((sin(alpha) + cos(alpha)) / (sqrt(2) * sin(pi / (2 * n))))
