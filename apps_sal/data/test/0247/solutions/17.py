def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def f(v, i1, i2):
    d = [v[i2][i] - v[i1][i] for i in range(len(v[i1]))]

    res = []
    for x in v:
        d2 = [x[i] - v[i1][i] for i in range(len(v[i1]))]
        if cross(d, d2) != 0:
            res.append(x)

    return res


n = int(input())
if n <= 4:
    print("YES")
    return

v = []
for i in range(n):
    v.append(list(map(int, input().split())))

ok = False
for first in range(3):
    if ok:
        break

    for second in range(first+1, 3):
        other = f(v, first, second)

        if len(other) <= 2:
            ok = True
            break

        remainder = f(other, 0, 1)

        if not remainder:
            ok = True


if ok:
    print("YES")
else:
    print("NO")

