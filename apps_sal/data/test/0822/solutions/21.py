def euclide(a, b):
    if b == 0:
        return a
    else:
        return euclide(b, a % b)


def ppcm(a, b):
    return b * (a // euclide(a, b))


def f(n, m, z):
    return z // ppcm(n, m)


(n, m, z) = tuple(map(int, input().split()))
print(f(n, m, z))
