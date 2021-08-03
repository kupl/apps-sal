def main():
    from sys import stdin
    l = stdin.read().splitlines()
    it, res, now = iter(enumerate(l)), [], 0
    next(it)
    for v in map(int, l[-1].split()):
        while now < v:
            i, s = next(it)
            c, t = list(map(int, s.split()))
            now += c * t
        res.append(i)
    print('\n'.join(map(str, res)))


def __starting_point():
    main()


__starting_point()
