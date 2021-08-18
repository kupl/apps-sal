a, b, c, d = list(map(int, input().split()))


def largest_div(n, m):
    while m > 0:
        rest = n % m
        n = m
        m = rest
    return n


if a / b == c / d:
    print("0/1")
else:
    if a / b > c / d:
        f_new_width = c * b
        f_upper = d * a - f_new_width
        f_lower = d * a
    else:
        f_new_height = d * a
        f_upper = c * b - f_new_height
        f_lower = c * b

    div = largest_div(f_upper, f_lower)
    print("/".join((str(int(f_upper / div)), str(int(f_lower / div)))))
