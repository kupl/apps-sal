m = int(input())


def rec(m):
    if m < 0:
        return (-1, 0)
    if m == 0:
        return (0, 0)
    a = int((m + 1e-09) ** (1 / 3))
    u = m - a ** 3
    v = a ** 3 - (a - 1) ** 3 - 1
    (x, y) = rec(u)
    (q, w) = rec(v)
    return max((x + 1, a ** 3 + y), (q + 1, (a - 1) ** 3 + w))


print(*rec(m))
