(n, m, q) = list(map(int, input().split()))


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


outer_inner_gcd = gcd(n, m)
line_outer_each = m // outer_inner_gcd
line_inner_each = n // outer_inner_gcd
for _ in range(q):
    (sx, sy, ex, ey) = list(map(int, input().split()))
    if sx == 1:
        lines_before_s = (sy - 1) // line_inner_each
    elif sx == 2:
        lines_before_s = (sy - 1) // line_outer_each
    if ex == 1:
        lines_before_e = (ey - 1) // line_inner_each
    elif ex == 2:
        lines_before_e = (ey - 1) // line_outer_each
    if lines_before_e == lines_before_s:
        print('YES')
    else:
        print('NO')
