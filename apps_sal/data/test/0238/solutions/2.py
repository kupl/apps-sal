n, m, k = [int(w) for w in input().split()]
a = [int(w) for w in input().split()]


def f(o):
    r = e = 0
    for i, x in enumerate(a):
        if i < o:
            continue
        if i % m == o:
            e -= k
            if e < -k:
                e = -k
        e += x
        if e > r:
            r = e
    return r


print(max(f(o) for o in range(m)))
