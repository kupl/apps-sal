from math import pi, sin, tan


def zvezda(n, r):
    alpha = (2 * pi) / n
    s1 = r * r * sin(alpha * 0.5) * sin(alpha * 0.5) / tan(0.5 * (alpha + 0.5 * alpha))
    s2 = 0.5 * (alpha - sin(alpha)) * r * r
    s3 = pi * r * r
    return format(s3 - n * (s2 + s1), '.10f')


N, R = [int(j) for j in input().split()]
print(zvezda(N, R))
