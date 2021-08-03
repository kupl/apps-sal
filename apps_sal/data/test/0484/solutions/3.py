n, a, b = list(map(int, input().split()))
ps = []
for i in range(n):
    ps.append(tuple(map(int, input().split())))

res = 0


def is_ok(p, a, b):
    return (p[0] <= a and p[1] <= b) or (p[0] <= b and p[1] <= a)


def is_pair_ok(p1, p2):
    an = a - p1[0]
    bn = b - p1[1]
    if an < 0 or bn < 0:
        return False
    return is_ok(p2, bn, a) or is_ok(p2, an, b)


for i1, p1 in enumerate(ps):
    for i2, p2 in enumerate(ps):
        if i1 == i2:
            continue
        cres = p1[0] * p1[1] + p2[0] * p2[1]
        if is_pair_ok(p1, p2) or is_pair_ok((p1[1], p1[0]), p2):
            res = max(cres, res)

print(res)
