def rec(m):
    if m <= 0:
        return (m, 0)
    a = int((m + 1e-09) ** (1 / 3))
    (x, y) = rec(m - a ** 3)
    (q, w) = rec(a ** 3 - (a - 1) ** 3 - 1)
    return max((x + 1, a ** 3 + y), (q + 1, (a - 1) ** 3 + w))


print(*rec(int(input())))
