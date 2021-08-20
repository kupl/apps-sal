def main():
    (h, v) = hv = ([0], [0])
    f = {'W': (v, -1), 'S': (v, 1), 'A': (h, -1), 'D': (h, 1)}.get
    for _ in range(int(input())):
        del h[1:], v[1:]
        for (l, d) in map(f, input()):
            l.append(l[-1] + d)
        x = y = 1
        for l in hv:
            (lh, a, n) = ((min(l), max(l)), 200001, 0)
            for b in filter(lh.__contains__, l):
                if a != b:
                    a = b
                    n += 1
            le = lh[1] - lh[0] + 1
            (x, y) = (y * le, x * (le - (n < 3 <= le)))
        print(x if x < y else y)


def __starting_point():
    main()


__starting_point()
