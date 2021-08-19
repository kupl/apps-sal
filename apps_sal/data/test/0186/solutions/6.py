(n, m) = [int(x) for x in input().split()]


def h1(k):
    return 6 * ((k - 1) // 2) + 2 * ((k - 1) % 2 + 1) if k > 0 else 0


def h2(k):
    return 3 + (k - 1) * 6 if k > 0 else 0


def h3(l):
    return 6 * k


def newx(k):
    return k - 2 if k % 6 == 4 else k - 4


def newy(k):
    return k - 6


(x, y, z) = (h1(n), h2(m), 0)
while max(x, y) > z + 6:
    z += 6
    if x > y:
        x = newx(x)
    else:
        y = newy(y)
print(max(x, y, z))
