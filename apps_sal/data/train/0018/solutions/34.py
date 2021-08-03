from math import sin, pi, radians


def solve():
    n = int(input()) * 2
    a = 180 * (n - 2) / n
    bc = (180 - a) / 2
    d = 0.5 / sin(radians(bc))
    return round(2 * (d**2 - 0.25)**0.5, 8)


for _ in range(int(input())):
    print(solve())
