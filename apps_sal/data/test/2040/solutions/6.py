
def add(c, v, p=0):
    assert(v < 10 and p < len(c))
    for i in range(p, len(c)):
        c[i] += v
        if c[i] >= 10:
            c[i] %= 10
            v = 1
        else:
            return
    c.append(v)


def find_min(xsum, l):
    csum = sum(l)
    if csum == xsum:
        return l

    if csum < xsum:
        for i, e in enumerate(l):
            delta = min(9 - e, xsum - csum)
            l[i] += delta
            csum += delta
        while csum != xsum:
            delta = min(9, xsum - csum)
            l.append(delta)
            csum += delta
    else:
        for i in range(0, len(l)):
            c = l[i]
            if c != 0:
                delta = 10 - c
                add(l, delta, i)
                csum = sum(l)
                if csum <= xsum:
                    return find_min(xsum, l)


n = int(input())

c = [0]
for i in range(n):
    b = int(input())
    find_min(b, c)
    print(''.join(map(str, c[::-1])))
    add(c, 1)
