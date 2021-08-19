MAXINT = 10 ** 10


def __starting_point():
    a, b, c = map(int, input().split())
    m, = map(int, input().split())
    usb, ps2 = [], []
    for _ in range(m):
        v, tp = input().split()
        if tp == 'USB':
            usb.append(int(v))
        else:
            ps2.append(int(v))
    usb.sort()
    ps2.sort()
    ui, pi = 0, 0
    un, pn = len(usb), len(ps2)
    #print(usb, ps2, un, pn)
    usb.append(MAXINT)
    ps2.append(MAXINT)
    res, cost = 0, 0
    while (ui < un and a > 0):
        res += 1
        cost += usb[ui]
        ui += 1
        a -= 1
    #print(res, cost)
    while (pi < pn and b > 0):
        res += 1
        cost += ps2[pi]
        pi += 1
        b -= 1
    #print(res, cost)
    while (c > 0 and (ui < un or pi < pn)):
        v = None
        if usb[ui] <= ps2[pi]:
            v = usb[ui]
            ui += 1
        else:
            v = ps2[pi]
            pi += 1
        res += 1
        cost += v
        c -= 1
    print(res, cost)


__starting_point()
