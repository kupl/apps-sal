(n, m) = list(map(int, input().split()))
(a, b, c, d) = ([], [], [], [])
for _ in range(n):
    (an, bn) = list(map(int, input().split()))
    a.append(an)
    b.append(bn)
for _ in range(m):
    (cn, dn) = list(map(int, input().split()))
    c.append(cn)
    d.append(dn)


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for i in range(n):
    minimum = 10 ** 9
    min_id = 0
    for j in range(m):
        ds = dist(a[i], b[i], c[j], d[j])
        if ds < minimum:
            minimum = ds
            min_id = j
    print(min_id + 1)
