n = int(input())
XY = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    XY.append((x, y))


def cross(a, b):
    return a.real * b.imag - b.real * a.imag


def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def circumcenter(a, b, c):
    bunshi = (a - b) * dot(c, c) + (b - c) * dot(a, a) + (c - a) * dot(b, b)
    bunbo = (a - b) * c.conjugate() + (b - c) * a.conjugate() + (c - a) * b.conjugate()
    if bunbo == 0:
        return (False, 0)
    return (True, bunshi / bunbo)


kouho = []
for i in range(n - 1):
    (a, b) = XY[i]
    z1 = complex(a, b)
    for j in range(i + 1, n):
        (c, d) = XY[j]
        z2 = complex(c, d)
        kouho.append((z1 + z2) / 2)
if n >= 3:
    for i in range(n - 2):
        (a, b) = XY[i]
        z1 = complex(a, b)
        for j in range(i + 1, n - 1):
            (c, d) = XY[j]
            z2 = complex(c, d)
            for k in range(j + 1, n):
                (e, f) = XY[k]
                z3 = complex(e, f)
                (flag, gaishin) = circumcenter(z1, z2, z3)
                if flag:
                    kouho.append(gaishin)
ans = 10 ** 10
for z in kouho:
    temp = 0
    for i in range(n):
        (x, y) = XY[i]
        z1 = complex(x, y)
        temp = max(temp, abs(z - z1))
    ans = min(ans, temp)
print(ans)
