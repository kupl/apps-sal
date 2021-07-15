from math import ceil

n, a, b = map(int, input().split())

s = 6 * n

if a * b >= s:
    na, nb = a, b
else:
    a1, b1 = min(a, b), max(a, b)
    q = [(x, ceil(s / x)) for x in range(a1, ceil(s ** .5)) if ceil(s / x) > b1]
    na, nb = min(q, key=lambda c: c[0] * c[1])
    if na < a:
        na, nb = nb, na

print(na * nb)
print(na, nb)
