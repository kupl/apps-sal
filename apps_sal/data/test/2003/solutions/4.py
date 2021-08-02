class D:
    u, v, n = None, None, 0


p = [1 << 30 - j for j in range(31)]


def sub(d, y):
    for j in p:
        d = d.u if y & j else d.v
        d.n -= 1


def add(d, y):
    for j in p:
        if not d.u:
            d.u, d.v = D(), D()
        d = d.u if y & j else d.v
        d.n += 1


def get(d, y):
    s = 0
    for j in p:
        if y & j:
            if d.v.n:
                d = d.v
                s += j
            else:
                d = d.u
        else:
            if d.u.n:
                d = d.u
                s += j
            else:
                d = d.v
    print(s)


d = D()
add(d, 0)
for i in range(int(input())):
    k, x = input().split()
    y = int(x)
    if k == '-':
        sub(d, y)
    elif k == '+':
        add(d, y)
    else:
        get(d, y)
