n = int(input())


def query(k):
    t = n
    g = (n + 1) // 2
    while t:
        if t < k:
            g -= t
            break
        t -= k
        g -= k
        t = t - t // 10
    if g <= 0:
        return 1
    else:
        return 0


def bs(l, r):
    if l == r:
        return l
    m = (l + r) // 2
    if query(m):
        return bs(l, m)
    else:
        return bs(m + 1, r)


print(bs(1, 1000000000000000000))
