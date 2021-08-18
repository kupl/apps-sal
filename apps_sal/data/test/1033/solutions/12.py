n, h = list(map(int, input().split()))


def g(d):
    if (d < h):
        return (d * (d + 1)) // 2
    d = d - h + 1
    dd = d // 2
    p = 2 * ((h - 1) * dd + (dd * (dd + 1)) // 2)
    if (d % 2 == 1):
        p += (h - 1 + dd + 1)
    return ((h - 1) * ((h - 1) + 1)) // 2 + p


a = 0
b = 10**20

while (a != b):
    c = (a + b) // 2
    if (n <= g(c)):
        b = c
    else:
        a = c + 1

print(a)
