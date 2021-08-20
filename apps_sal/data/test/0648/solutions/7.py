def sigma(n):
    return n * (n + 1) // 2


def banans(p, q):
    return (p + 1) * sigma(q) + (q + 1) * sigma(p)


(m, b) = [int(x) for x in input().split()]
r = 0
for i in range(m * b + 1):
    if i % m == 0:
        (p, q) = (i, b - i // m)
        r = max(r, banans(p, q))
print(r)
