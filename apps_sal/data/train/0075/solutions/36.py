from math import pi, sin


def solve(n):
    r = pi / (4 * n)
    m = 1 / sin(r)
    return round(m / 2, 9)


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
