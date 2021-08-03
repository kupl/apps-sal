def main():
    hh, vv, r = [0], [0], []
    f = {'W': (vv, -1), 'S': (vv, 1), 'A': (hh, -1), 'D': (hh, 1)}.get
    for _ in range(int(input())):
        del vv[1:], hh[1:], r[:]
        for l, d in map(f, input()):
            l.append(l[-1] + d)
        for l in hh, vv:
            mi, ma = min(l), max(l)
            a, tmp = mi - 1, []
            for b in filter((mi, ma).__contains__, l):
                if a != b:
                    a = b
                    tmp.append(a)
            ma -= mi - 1
            r.append(ma)
            if len(tmp) < 3 <= ma:
                ma -= 1
            r.append(ma)
        print(min((r[0] * r[3], r[1] * r[2])))


def __starting_point():
    main()


__starting_point()
