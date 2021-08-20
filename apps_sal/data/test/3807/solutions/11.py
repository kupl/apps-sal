def g(m, s, n):
    k = int(m ** (1 / 3))
    if m == 0 or k == 1:
        return (s + m, n + m)
    (x, y) = (k ** 3, (k - 1) ** 3)
    a = g(m - x, s + x, n + 1)
    b = g(x - y - 1, s + y, n + 1)
    return b if a[1] < b[1] else a


(s, n) = g(int(input()), 0, 0)
print(n, s)
