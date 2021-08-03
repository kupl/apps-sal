from itertools import chain

C = 0


def main():
    input()
    ls = list(map(int, input()))
    n = len(ls)
    a = ls[-1]
    for stop, b in enumerate(ls):
        if b != a:
            break
    else:
        print('0' * n)
        return
    ls = ls[stop:] + ls[:stop]
    a, l = ls[0], []
    start = ma = tail = 0
    for stop, b in enumerate(ls):
        if b != a:
            le = stop - start
            if ma < le:
                ma, tail = le, (b - a) % 10
                l.clear()
                l.append(start)
            elif ma == le:
                tl = (b - a) % 10
                if tail > tl:
                    tail = tl
                    l.clear()
                    l.append(start)
                elif tail == tl:
                    l.append(start)
            a, start = b, stop
    le = n - start
    if ma < le:
        l.clear()
        l.append(start)
    elif ma == le:
        tl = (ls[0] - a) % 10
        if tail > tl:
            l.clear()
            l.append(start)
        elif tail == tl:
            l.append(start)
    for i, start in enumerate(l):
        base = ls[start]
        l[i] = ''.join(str((a - base) % 10) for a in chain(ls[start:], ls[:start]))
    print(min(l))


def __starting_point():
    main()


__starting_point()
