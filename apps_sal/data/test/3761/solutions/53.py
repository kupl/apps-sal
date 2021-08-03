
def search(arr, start):
    s = set()
    s.add(start)
    for i in arr:
        ns = set()
        for j in s:
            ns.add(j + i)
            ns.add(j - i)
        s = ns
    return s


def main():
    t = 0
    xd, yd = [], []

    inst = list(input())
    x, y = list(map(int, input().split()))

    xcum = 0
    ycum = 0
    first = True

    startx = 0
    for s in inst:
        if s == 'T':
            t += 1
            t %= 2
            if first:
                startx = xcum
                xcum = 0
                first = False
                continue
            if xcum > 0:
                xd.append(xcum)
                xcum = 0
            if ycum > 0:
                yd.append(ycum)
                ycum = 0
        else:
            if t == 0:
                xcum += 1
            else:
                ycum += 1
    if first:
        startx = xcum
    elif xcum > 0:
        xd.append(xcum)
        xcum = 0
    if ycum > 0:
        yd.append(ycum)
        ycum = 0

    # print(startx)
    # print(xd, yd)
    # print(search(xd, startx), search(yd, 0))
    if x in search(xd, startx) and y in search(yd, 0):
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
