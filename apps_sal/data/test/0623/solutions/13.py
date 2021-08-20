import math
(x, y) = (int(z) for z in input().split())
a = min(x, y)
b = max(x, y)


def g(a, b, res):
    if a * b == 0:
        return res
    if a * b == 1:
        return res
    k = math.ceil((b - a) / 3)
    if k == 0:
        k = 1
    a += k
    b -= 2 * k
    m = min(a, b)
    p = max(a, b)
    return g(m, p, res + k)


print(g(a, b, 0))
