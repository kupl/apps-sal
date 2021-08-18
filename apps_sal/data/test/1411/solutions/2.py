def solve(ls):

    ls.sort(key=lambda q: q[1] - q[0])

    m = sum(si for a, b, si in ls)

    k = s * (m // s)

    n = m - k

    x = y = z = 0

    for a, b, si in ls:

        if k >= si:

            k -= si

            z += si * a

        elif k:

            z += k * a

            x = (si - k) * a

            y = (si - k) * b

            k = 0

        else:

            x += si * a

            y += si * b

    return x, y, z, n


n, s = list(map(int, input().split()))

first = []

second = []

for i in range(n):

    si, ai, bi = list(map(int, input().split()))

    if ai > bi:

        first.append((ai, bi, si))

    else:

        second.append((bi, ai, si))

x1, y1, z1, n1 = solve(first)

x2, y2, z2, n2 = solve(second)

d = x1 + x2 if n1 + n2 > s else max(x1 + y2, x2 + y1)

print(z1 + z2 + d)
