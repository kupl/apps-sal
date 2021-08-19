IN = input


def rint():
    return int(IN())


def rmint():
    return list(map(int, IN().split()))


def rlist():
    return list(rmint())


w = [0, 1, 2, 0, 2, 1, 0]
h = rlist()
ans = 0


def g(x):
    p = w[x:]
    a = h[:]
    v = 0
    for f in p:
        if not a[f]:
            return v
        a[f] -= 1
        v += 1
    u = min([a[0] // 3, a[1] // 2, a[2] // 2])
    a[0] -= u * 3
    a[1] -= u * 2
    a[2] -= u * 2
    v += u * 7
    for f in w:
        if not a[f]:
            return v
        a[f] -= 1
        v += 1
    return v


for i in range(7):
    ans = max(ans, g(i))
print(ans)
