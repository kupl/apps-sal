import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


n, m, q = map(int, input().split())

l = lcm(n, m)

for _ in range(q):
    sx, sy, ex, ey = map(int, input().split())

    sy -= 1
    ey -= 1

    if sx == 1:
        s_area = (m * sy) // l
    elif sx == 2:
        s_area = (n * sy) // l
    if ex == 1:
        e_area = (m * ey) // l
    elif ex == 2:
        e_area = (n * ey) // l

    if s_area == e_area:
        print("YES")
    else:
        print("NO")
